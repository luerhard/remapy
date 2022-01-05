import numpy as np
from remapy import model
from remapy.model.item import Item
from pathlib import Path


class Collection(Item):

    #
    # CTOR
    #
    def __init__(self, metadata, parent):
        super(Collection, self).__init__(metadata, parent)
        self.state = model.item.STATE_SYNCED
        pass


    #
    # Getter and setter
    #
    def current_page(self):
        return "-"


    #
    # Functions
    #
    def add_child(self, child: Item):
        self._children.append(child)
        child.add_state_listener(self.listen_child_state_change)


    def sync(self):
        if self.is_root():
            return

        # Write metadata of collection and of all parents to ensure 
        # that we have the same information available when we are offline
        self._write_remapy_file()
        self.parent().sync()


    def delete(self):
        
        for child in self._children:
            ok = child.delete()
            if not ok:
                return False

        ok = self.rm_client.delete_item(self.id(), self.version())
        if ok:
            self._update_state(state=model.item.STATE_DELETED)
        return ok


    def full_name(self):
        if self.parent() is None:
            return ""
            
        if self.parent().parent() is None:
            return self.name()
            
        return "%s/%s" % (self.parent().full_name(), self.name())


    def _update_state(self, state):
        if self.is_root():
            return 
            
        self.state = state
        self._update_state_listener()
    

    def get_exact_children_count(self):
        """ Returns exact number of children and children of children etc.
            and it counts itself.
        
            return: (num_documents, num_collections)
        """
        count = [0, 1]
        for child in self._children:
            if child.is_document():
                count[0] += 1
                continue
            child_count = child.get_exact_children_count()
            count = np.add(count, child_count)
            
        return count
    

    def is_parent_of(self, item):
        for child in self._children:
            if child.id() == item.id():
                return True
            
            if child.is_parent_of(item):
                return True
        
        return False
    

    def listen_child_state_change(self, item):
        if item.state == model.item.STATE_DELETED:
            self._children.remove(item)
            return
        
        # Check sync stage
        for child in self._children:
            if child.state == model.item.STATE_SYNCING:
                self._update_state(model.item.STATE_SYNCING)
                return
        self._update_state(model.item.STATE_SYNCED)
    

    def create_backup(self, path):
        Path(path).mkdir(parents=True, exist_ok=True)

    
    def update_state(self):
        pass
