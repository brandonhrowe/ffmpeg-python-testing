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

detour = ffmpy.FFmpeg(
  inputs={"https://archive.org/download/Detour_movie/Detour.mp4": '-hide_banner'},
  outputs={"pipe:1": '-an -filter:v "select=\'gt(scene, 0.3)\', showinfo" -f null'}
)
detour.cmd
stdout, stderr_detour = detour.run(stdout=subprocess.PIPE, stderr=subprocess.PIPE)

doa = ffmpy.FFmpeg(
  inputs={"https://archive.org/download/doa_1949/doa_1949.mp4": '-hide_banner'},
  outputs={"pipe:1": '-an -filter:v "select=\'gt(scene, 0.3)\', showinfo" -f null'}
)
doa.cmd
stdout_doa, stderr_doa = doa.run(stdout=subprocess.PIPE, stderr=subprocess.PIPE)

output = stderr_detour.decode("utf-8").split("\n")
filtered_output = list(filter(lambda x : "Parsed_showinfo_1" in x and "pts_time" in x, output))
final_output = list(map(lambda y : ((next(filter(lambda z : z.startswith("pts_time"), y.split(" ")), None)).split(":"))[1], filtered_output))
print(final_output)
shot_num = len(final_output)
random_idx = random.randint(0, shot_num)

output_doa = stderr_doa.decode("utf-8").split("\n")
filtered_output_doa = list(filter(lambda x : "Parsed_showinfo_1" in x and "pts_time" in x, output_doa))
final_output_doa = list(map(lambda y : ((next(filter(lambda z : z.startswith("pts_time"), y.split(" ")), None)).split(":"))[1], filtered_output_doa))
print(final_output_doa)
shot_num_doa = len(final_output_doa)
random_idx_doa = random.randint(0, shot_num_doa)

ff2_detour = ffmpy.FFmpeg(
  inputs={"https://archive.org/download/Detour_movie/Detour.mp4": f'-ss {final_output[random_idx]} -to {round(float(final_output[random_idx + random.randint(1, 4)]) - (2 / 29.97), 2)}'},
  outputs={"test_detour.mp4":None}
)
ff2_detour.cmd
ff2_detour.run()

ff2_doa = ffmpy.FFmpeg(
  inputs={"https://archive.org/download/doa_1949/doa_1949.mp4": f'-ss {final_output_doa[random_idx_doa]} -to {round(float(final_output_doa[random_idx_doa + random.randint(1, 3)]) - (2 / 29.97), 2)}'},
  outputs={"test_doa.mp4":None}
)
ff2_doa.cmd
ff2_doa.run()

ff3_merge = ffmpy.FFmpeg(
  inputs={"ffmpeg_demuxer_test.txt": "-f concat"},
  outputs={"test_concat.mp4": "-c copy"}
)

ff3_merge.cmd
ff3_merge.run()
