+++
draft = false
date = "2012-01-06"
title = "Install Android Market on Coby Kyros MID7012 (or most other tablets running Android 2.3.3)"
tags = ["blog", "tutorial", "android"]
highlight = true
math = false
summary = """
Get Android Market (Google Play App Store) on your older Android device!
"""

[header]
  caption = "Image: Coby Kyros Tablet"
  image = "banners/android-coby-kyros-tablet.jpg"
  preview = false

+++

{{% alert note %}}
This tutorial originally appeared on my (Alex's) blog on Northwest Tech Experience (nwteche.com). That website has been removed. I have moved some of the content I wrote, including this page, to this website of mine. I may have edited the original content for clarity.
{{% /alert %}}

# Background

This Christmas I put the [Coby Kyros MID7012 tablet](https://www.amazon.com/gp/product/B005HUH88K) (which only runs Android 2.3.3) on my wish list. I was surprised when I actually received it! By that time, I had decided I didn’t really need it.

The [Kyros 7012](https://www.amazon.com/gp/product/B005HUH88K) and others don’t have the [Android Market](https://en.wikipedia.org/wiki/Google_Play#History) installed out of the box. It would seem like all you’d need to do is install a few .apk files and you’d be good, right? Well all but two articles I read online were not like that at all. Most required you to [root](https://en.wikipedia.org/wiki/Rooting_(Android)) the device. Although rooting itself can be undone, certain things done with rooting privileges cannot. Not to mention the fact that “rooting” the tablet most likely voids the warranty on the device. So, in short, it doesn’t seem like “doing it right the first time” is very popular with people installing the Android Market. That is why I wanted to throw in my two cents about this so that more people can do this right and not mess up their devices.

After some research, I found a method that worked for me. It is based off a YouTube tutorial. If you go on YouTube, it’s the first one that pops up if you search “install android market on coby” I believe. Here’s the actual URL: http://www.youtube.com/watch?v=6BrWSC2uiAg

## Release of Liability

**NOTE:** I, ALEXANDER HOGEN, AND ANY OTHER INDIVIDUAL OR COMPANY ASSOCIATED WITH MYSELF SHALL NOT BE HELD RESPONSIBLE FOR ANY DAMAGE, LOSS OF DATA, LOSS OF FUNCTIONALITY OR
ANY OTHER OUTCOME AS A RESULT OF FOLLOWING THIS TUTORIAL. THE USER RECOGNIZES THAT THERE ARE CERTAIN INHERENT RISKS ASSOCIATED WITH PERFORMING THE OPERATIONS DESCRIBED IN THIS TUTORIAL AND THE USER ASSUMES FULL RESPONSIBILITY FOR ANY UNDESIRABLE OUTCOME DURING OR AFTER PERFORMING THE STEPS DESCRIBED ON THIS WEBSITE. 

I put that notification up in case someone messes up their device by following this tutorial, although I *seriously* doubt they will. These steps aren't hard and there is no rooting or "jail-breaking" involved. Okay, here we go.

# Instructions

1. On your computer, download the “Android Market_install_files.zip” below and unzip all the files to a convenient location (say, your desktop). [**Android Market_install_files.zip**](/downloads/Android-Market_install_files.zip)

2. Now connect the tablet to your PC and put these files on your tablet’s SD card or internal memory. If your not sure how to do this, consult your [product manual](https://web.archive.org/web/20130822214307/http://cobyusa.com/files/manuals/MID7012_MN.pdf) (on page 30 I think). I stuck the files in the “downloads” folder on the device itself.

3. After the files have finished transferring, disconnect the tablet from your PC.

4. Go to your file viewer app. On my tablet, they installed “ES File Explorer”. Yours should have a similar file explorer program.

5. Now find where you put those .apk files. I put mine in the “downloads” folder.

6. Ok, now you are going to install them in a specific order. (Just tap on the file to install. Hit “Done” after each one. **DON’T** RUN THEM AFTER THEY INSTALL!) Here is the order:

    1. OneTimeInitializer.apk
    2. SetupWizard.apk
    3. GoogleServicesFramework-signed.apk
    4. com.android.vending.3.3.12.apk

7. Ok, this step is important. **DO NOT** GO TO THE HOME SCREEN!!. Press and hold the power button on the tablet and turn it off.

8. Now turn it back on!

9. After start-up, you will see a menu with two options. Check the “Use this as default” box on the bottom, then select the option on top (“Launcher”). You don’t want to set up anything. You just want to use the regular initializer.

10. Make sure you are connected to a wireless network (WIFI). If not, get your tablet connected.

11. Now that your connected, go to the Apps list (by tapping the box made of little squares that’s either on the bottom or right hand side of your screen).

12. You should see the Android Market icon in this list. Go ahead and open it. Since this is the first run, you’ll need to enter your Google Account information and accept the license agreement.The Android Market will filter out most apps that won’t work with your tablet.

**You should be good to go. Enjoy your new apps!**

