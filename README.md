# crowd_pong
Crowd Pong (c) by Aaron Ciuffo

Crowd Pong is licensed under a
Creative Commons Atrribution-ShareAlike 3.0 Unported Licenses

You should have received a copy of the license along with this
work.  If not, see <http://creativecommons.org/licenses/by/3.0/>.

These scripts output a string of values between 1 and -1 on a web socket for 
controling a pong-like game using relative ratios of two colors visible to a web-cam.

Scripts provided as both ipython notebooks and python scripts.

**crowd_pong_video_capture**
Requirements: 
  * OpenCV 2.4 (On OS X: brew tap homebrew/science; brew install opencv)
  * Python 2.7 (On OS X: brew install python27)
  * OpenCV python bindings (pip install opencv)
  * numpy python module (pip install numpy)
  * websocket python module (pip install websocket-client)
  * tornado websocket echo server (pip install tornado[all]

Function:
Captures frames from a live video stream and provides a method for selecting from
two different colors. The relative ratio of colorA to colorB affects the output of a 
value between -1 and 1. The greater proportion of one color over the other affects
the velocity of the pong bat. The output value is sent as a message to a local
websocket server that rebroadcasts.  The game interface listens on 
ws://localhost/9000/ws.

The video capture script provides a live view and two masked views to show sampled
colorA and colorB.  The script also provides two sets of controls for fine-tuning the
color range, hue and saturation limits for each color.

  Control panels:
  Hue (+/-): general selected color range 
  S (+): saturation of color (darker colors have a higer saturation value)
  V (+/-): value of color (brigter colors have a higher value)
  CR: Preset color range to help quickly choose colors

See cp-instructions.txt for more information.

**tornado-websocket-server**
Requirements:
  * Python 2.7
  * tornado python module (pip install tornado[all])

Function:
Websocket server that listens on ws://localhost/9000/ws for messages and then 
rebroadcasts incoming messages to all connected clients.

**write_to_websocket**
Requirements:
  * Python 2.7
  * websocket-client (pip install websocket-client)

Fucntion: 
Test client for sending simulated output to websocket server.  
