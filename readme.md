Spotify Song Discovery
======================
Pretty self explanatory but basically adds 20 unique random songs to your spotify liked songs playlist

Important
==========
Make sure you go to https://developer.spotify.com/dashboard/applications and create an app for this project

Also go to https://developer.spotify.com/dashboard/applications/(application-id)/users scroll down and click on add new user to add your gmail to access your application

In https://developer.spotify.com/dashboard/applications/(application-id)/users click on edit settings and change the 'Redirect url' value to 'https://oauth.pstmn.io/v1/browser-callback'

To get the developer token and connect this app to your spotify account go to https://developer.spotify.com/console/post-playlist-tracks/ and scroll down\
Click on the 'get token button'\
In the 'Required scopes for this endpoint:' select 'playlist-modify-private'\
And\
In the 'You can optionally ask for any of these scopes:' choose all the scopes except for 'playlist-read-collaborative' and 'playlist-read-public'

The spotify token expires every one hour so go back to https://developer.spotify.com/console/post-playlist-tracks/ and repeat the above steps

If there is a key error:
========================
->Go to line 26 and indent it once spotify_client.py \
->If there still is a key error de-indent line 26 in spotify_client.py\
Repeat as necessary

WARNING: Doesn't work anymore in correspondence with the new spotify update
