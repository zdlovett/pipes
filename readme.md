# Overview

The goal of the app is to provide the user with a way to share files 
in a ephemeral fashion, with no uploading to cloud storage nonsense. 

The expected use pattern is as follows:

1) User navigates to starting page
page provides two options:
* new pipe
* connect to pipe

if the user selects new pipe, they are sent to a page with a uuid displayed at the top, and
can send that uuid to other people. 
Other users can then use that uuid with the connect to pipe option 
to be join into the same session. 

Once a user is in a session they can "upload" files by dragging and dropping 
onto the page. This will need to be handled by local JS since the goal would be
for that file to not actually be uploaded until another user has requested the file.

Again, eventually this should be something that happens over webRTC with no bytes of the 
payload ever passing though the server connection. 




# Things to Solve
* Lifecycle management of the pipe/pipe uuid when to invalidate the pipe? On last user disconnect?
* all of the js bits lol 
* should the app actually just be a js webapp that is served as a single page, and then a combo api server / ICE / TURN / whatever server(s) in the background to make it all work?
