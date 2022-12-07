import streamlit as st
import cv2 
import time
video_file= st.file_uploader("Upload a video")

def write_file(filename  , data):
    with open (filename,"wb") as out:
        out.write(data.getbuffer())

def write_frame(frame,path, file_name):     
    cv2.imwrite(f"{path}/{file_name}",frame)


def read_video(filename): 	
   vid_capture = cv2.VideoCapture('output/sample_video.mp4')
   return vid_capture

def show_frame(image):
    st.image(image)

def get_video_details(video_object):
    frame_width = int(video_object.get(3))
    frame_height = int(video_object.get(4))
    original_fps = int(video_object.get(5))
    frame_size = (frame_width,frame_height)
    frame_count = int(video_object.get(7))
    fps = 20
    frame_meta =  {
                    "width":frame_width , "height": frame_height , 
                    "size":frame_size,"fps":fps,"frames":frame_count,
                    "original_fps":original_fps
                   }
    return frame_meta

if video_file:
   st.text(type(video_file))
   file_name = video_file.name
   print(f"file name = {file_name}")
   st.video(video_file)
   
   write_file("output/sample_video.mp4",video_file)
   st.text("Completed writing sample video")

   vid_capture = read_video("output/sample_video.mp4")
   if (vid_capture.isOpened() == False):
      st.text("Error opening the video file")
   else:
      meta = get_video_details(vid_capture)
      st.text(meta)

   result = st.button("Extract Images")
   if result:
      i= 0
      while(vid_capture.isOpened()):
         i = i+1 
         ret, frame = vid_capture.read()
         if ret == True and i < 500:
            # show_frame(frame)
            image_name=f"soccer_image_{i}.jpeg"
            write_frame(frame,"output/images",image_name)
            key = cv2.waitKey(20)
            if key == ord('q'):
               break
         else:
            break
      st.text("Extracting images completed")
   vid_capture.release()
   cv2.destroyAllWindows()




