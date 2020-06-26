# RemaPy Explorer

RemaPy is an open-source file explorer for your reMarkable tablet that uses the
reMarkable cloud. You can upload documents (via copy and paste), open notebooks
and annotated pdfs and delete documents or collections. RemaPy is written in
Python and only tested on Linux. Especially for OSX we have currently some 
problems with RemaPy. See also [Issue 10](https://github.com/peerdavid/remapy/issues/10).
A "how to install", the software architecture and FAQ's 
can be found in the [wiki](https://github.com/peerdavid/RemaPy/wiki).

*WARNING: This project is not affiliated to, 
nor endorsed by, reMarkable AS. I am not responsible for any 
damage done to your device or your data 
due to the use of this software.*

*NOTE: The newest delete logic (trash) is already implemented in RemaPy and 
therefore your reMarkable tablet should run with software version 2.2*


# Features 
## Overview
<img src="doc/explorer.png" />

## Open with or without annotations
With RemaPy you can open the annotated pdf file (double click). You can also
open the original file without annotations or you can open the file containing
only the pages that are annotated (right-click). If evince is installed on your
system, RemaPy opens the same page as on your tablet. Note that if you open a
collection, all child items are opened recursively.

## Upload pdfs, epubs or webpages
If you copy and paste a file from your file explorer into RemaPy, it
is uploaded if the file ends with .pdf or .epub. Select the base folder 
(or any item in this folder) where the file should be located after the upload.
If you copy and paste a URL, the given website is automatically converted into
a pdf and uploaded to your reMarkable. Note that some heuristics
are implemented to accepts the "terms of usage" of pages automatically, 
but this will not work in every case 
(see also [FAQ](https://github.com/peerdavid/RemaPy/wiki)). Please also note
that some additional packages must be installed to use this feature 
(pdfkit and wkhtmltopdf).

## Custom colors
Custom colors for individual layers are used by RemaPy for rendering
if the layer name contains a '#' followed by a valid color name or 
[hex code](https://www.color-hex.com/).
For example "Layer1 #ffee11" is rendered with hex color #ffee11 or "Layer 2 #red" 
is rendered in red. The hex code also supports alpha values (e.g. #ffee11dd).
Therefore you can easily hide layers in the rendering process by setting the last
two values of the hex code to zero: #xxxxxx00.
<img src="doc/custom_colors.png" />

## Filter
You can use the filter (upper right) to display only a subset of documents and
collections (not case sensitive). To search only for bookmarked items, start
your search string with "!b". For example to search for all bookmarked items
that contain "RemaPy", enter "!b RemaPy".
To search all items that contain "RemaPy" enter only "RemaPy".

## Backup
In the settings tab you can find an option "Backup". This creates a 
backup of all your annotated pdf files into the given folder. Note that it 
it is not possible to backup or restore the *raw* items.

## Trash
RemaPy uses the same delete logic than the ReMarkable V2.2. Therefore if
you delete a collection or a document, it is moved into the trash.
You can delete the item completely from the tablet if you delete it inside
the trash. You can also restore files that are deleted from the trash.
*NOTE: If you create a backup, the trash is also included.*

## Other features
 - Rename or delete items
 - Toggle bookmark
 - Offline mode


# Acknowledgments
[1] Python reMarkable api, https://github.com/subutux/rmapy <br />
[2] Golang reMarkable tool, https://github.com/juruen/rmapi/ <br />
[3] Icons made by Freepik, Smashicons, Pixel Perfect, iconixar  srip, 
Good ware, prettycons, Payungkead, bqlqn from www.flaticon.com <br />
