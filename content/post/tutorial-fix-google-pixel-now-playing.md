# My fix for Google Pixel Now Playing

A few weeks ago, I noticed the Now Playing feature of my new Google Pixel 3 phone stopped working. The shortcut/icon was still on my home screen, however it hadn't detected any songs recently.

# Testing if Now Playing is broken

I wanted to quickly verify that the reason Now Playing history looked old was in fact because Now Playing had stopped working. It is possible for the phone to be muffled by a pocket or out of range and not detect songs. So i eliminated this possibility by running a quick test.

It's been reported that "Rap god" by Eminim is known to be detected by Now Playing. So I'll use that.

- Navigate to Now Playing history, either by tapping the shortcut on your home screen or by going to `Settings > Sounds > Now Playing > Now Playing history` (If the history option is even available. It was missing for me when this problem occurred.)

- Start playing the test song on another device. 

- Wait for up to 1 minute to see if Now Playing detects the song. 

- If the song does not appear in your Now Playing history or on the home screen after a minute, it's likely broken.

# Reset Now Playing 

Essentially what I did is clear all app data, uninstall, and then reinstall the applications that looked like they were related to Now Playing.

- Navigate to `Settings > Apps & Notifications > See all N apps`

- Tap `Action Services > Storage` and then tap the `Clear storage` button

- Go back to the apps list and find the "Pixel Ambient Services" app. Tap `Storage` and tap the `Clear storage` button here as well.

- Now that both apps' data has been cleared, I went ahead and uninstalled them. This step may not be necessary but I did it anyway.

    - Find the "Actions Services" and "Pixel Ambient Services" apps in the apps list again
    - Tap `Force stop` and tap `OK` at the prompt
    - Next tap `Disable` and accept the two prompts. This reverts any updates and replaces it with the original app your phone came with out of the box. Now tap `Enable` to turn the app back on.
    - Do the above steps for both apps.
    - Now open Google Play Store app. Tap the hamburger menu on the top left, tap `My apps and games` and tap the `Updates` tab. You may need to hit the refresh button to see updates for the two apps we reverted back to factory versions.
    - Tap the `Update All`

- Now we'll get Now Playing re-enabled. To do this, we have to open the Pixel tips/tutorial app that you encoutered when you powered up your phone for the first time. Confusingly, to open "Pixel Tips" do this...
    - Find "Actions Services" app in the "Installed" tab of Google Play Store.
    - Tap `Open`. Notice the title of the app we just opened says "Pixel Tips", not "Actions Services". Very annoying... Oh well...
    - Tap `Maximize Google` near the bottom of the screen
    - Tap the right arrow a few times to get over to the "Now Playing" screen.
    - Tap `Turn on in settings`
    - This should take you to Now Playing in settings where you could enable notifications on the lock screen.

At this point, it started working for me. 

### Some miscallaneous notes

- It seems Pixel Tips is also accessable by going to `Settings > Tips & Support > Go to Tips`

- After re-enabling and updating the Pixel Ambient Services app, you might be able to simply open the Settings app and at the top of the screen there might be a box with a suggestion to turn on Now Playing. 


I hope this helps!
