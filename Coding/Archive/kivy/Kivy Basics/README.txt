in the quest to get kivy working again 7_28_2021 see related bookmarks

applying:
https://stackoverflow.com/questions/49482753/sdl2-importerror-dll-load-failed-the-specified-module-could-not-be-found-and

ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
kivy-examples 2.0.0 requires kivy-deps.sdl2~=0.3.1; sys_platform == "win32", but you have kivy-deps-sdl2 0.4.2 which is incompatible.

now this works but nothing shows up
we are still in this circomstance this works and nothing shows up meanwhile our other kivy project work great.
fixed by changing the name of the kivy file from my_old.kv to my.kv

So this is now a very generic kivy app with 3 field for inputs and popups for outputs

The outputs need to be mapped out this may contain the key the kivy output functions
