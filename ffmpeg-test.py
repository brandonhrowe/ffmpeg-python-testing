import ffmpeg
import random
import ffmpy
import subprocess

# in1 = ffmpeg.input('https://archive.org/download/Detour_movie/Detour.mp4', ss=60, t=90)
# in2 = ffmpeg.input('https://archive.org/download/Detour_movie/Detour.mp4', ss=240, t=90)
# v1 = in1.video.hflip()
# a1 = in1.audio
# v2 = in2.video.filter('reverse').filter('hue', s=0)
# a2 = in2.audio.filter('areverse').filter('aphaser')
# joined = ffmpeg.concat(v1, a1, v2, a2, v=1, a=1).node
# v3 = joined[0]
# a3 = joined[1].filter('volume', 0.8)
# out = ffmpeg.output(v3, a3, 'out.mp4')
# out.run()

# main = ffmpeg.input('https://archive.org/download/Detour_movie/Detour.mp4', t=90)
# main = ffmpeg.input('WoTClip.mov')
# logo = ffmpeg.input('MMofaStreet.jpg')

# (
#     ffmpeg
#     .filter([main, logo], 'overlay', 500, 500)
#     .output('WoT_Output_Burnin.mp4')
#     .run()
# )

# probe = ffmpeg.probe('https://archive.org/download/Detour_movie/Detour.mp4')
# print(probe)

ff = ffmpy.FFmpeg(
  inputs={"https://archive.org/download/Detour_movie/Detour.mp4": '-hide_banner'},
  outputs={"pipe:1": '-an -filter:v "select=\'gt(scene, 0.4)\', showinfo" -f null'}
)
ff.cmd
stdout, stderr = ff.run(stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# print("stdout:", stdout)
# print("stderr:", stderr)
# output = filter(lambda x : "[Parsed_showinfo" in x, stderr.decode("utf-8").split("\n"))
output = stderr.decode("utf-8").split("\n")
filtered_output = list(filter(lambda x : "Parsed_showinfo_1" in x and "pts_time" in x, output))
final_output = list(map(lambda y : ((next(filter(lambda z : z.startswith("pts_time"), y.split(" ")), None)).split(":"))[1], filtered_output))
print(final_output)
