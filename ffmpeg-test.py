import os
import ffmpeg
import random
import ffmpy
import subprocess
from internetarchive import search_items, get_item
from threading import Timer

# # LOOP THROUGH ALL TITLES IN FILM_NOIR COLLECTION
# for i in search_items('collection:Movie_Trailers'):
    # identifier = i['identifier']
    # item = get_item(identifier)
    # file_name = next(filter(lambda x: ".mp4" in x['name'], item.files), None)[
    #     'name']
    # print(identifier)
    # print(file_name)
    # ff = ffmpy.FFmpeg(
    #     inputs={f"https://archive.org/download/{identifier}/{file_name}": '-hide_banner'},
    #     outputs={
    #         "pipe:1": '-an -filter:v "select=\'gt(scene, 0.3)\', showinfo" -f null'}
    # )
    # ff.cmd
    # stdout, stderr = ff.run(stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # shot_log = stderr.decode("utf-8").split("\n")
    # filtered_output = list(
    #     filter(lambda x: "Parsed_showinfo_1" in x and "pts_time" in x, shot_log))
    # final_output = list(map(lambda y: ((next(filter(lambda z: z.startswith(
    #     "pts_time"), y.split(" ")), None)).split(":"))[1], filtered_output))
    # print(final_output)

    # # SAMPLE FOR CREATING CLIPS FROM SHOT DATA AND CONCATENATING INTO SINGLE FILE
    # detour = ffmpy.FFmpeg(
    #   inputs={"https://archive.org/download/BerlinSymphonyofaGreatCity/BERLIN_512kb.mp4": '-hide_banner'},
    #   outputs={"pipe:1": '-an -filter:v "select=\'gt(scene, 0.3)\', showinfo" -f null'}
    # )
# detour = ffmpy.FFmpeg(
#     inputs={"https://archive.org/download/12AngryMen1957Trailer/12AngryMen1957trailer.mp4": '-hide_banner'},
#     outputs={
#         "pipe:1": '-an -filter:v "select=\'gt(scene, 0.3)\', showinfo" -f null'}
# )
detour = ffmpy.FFmpeg(
  inputs={"https://archive.org/download/Detour_movie/Detour.mp4": '-hide_banner'},
  outputs={"pipe:1": '-an -filter:v "select=\'gt(scene, 0.3)\', showinfo" -f null'}
)
detour.cmd
stdout, stderr_detour = detour.run(
    stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# doa = ffmpy.FFmpeg(
#   inputs={"https://archive.org/download/AliceInWonderland1803/AliceInWonderland1803.mp4": '-hide_banner'},
#   outputs={"pipe:1": '-an -filter:v "select=\'gt(scene, 0.3)\', showinfo" -f null'}
# )
# doa = ffmpy.FFmpeg(
#     inputs={"https://archive.org/download/2001ASpaceOdysseyTrailer/2001ASpaceOdysseyTrailer.mp4": '-hide_banner'},
#     outputs={
#         "pipe:1": '-an -filter:v "select=\'gt(scene, 0.3)\', showinfo" -f null'}
# )
doa = ffmpy.FFmpeg(
  inputs={"https://archive.org/download/doa_1949/doa_1949.mp4": '-hide_banner'},
  outputs={"pipe:1": '-an -filter:v "select=\'gt(scene, 0.3)\', showinfo" -f null'}
)
doa.cmd
stdout_doa, stderr_doa = doa.run(
    stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# stranger = ffmpy.FFmpeg(
#   inputs={"https://archive.org/download/20000LeaguesUndertheSea/20000_Leagues_Under_the_Sea_512kb.mp4": '-hide_banner'},
#   outputs={"pipe:1": '-an -filter:v "select=\'gt(scene, 0.3)\', showinfo" -f null'}
# )
# stranger = ffmpy.FFmpeg(
#     inputs={"https://archive.org/download/49thParallelTrailer/49thParallelTrailer.mp4": '-hide_banner'},
#     outputs={
#         "pipe:1": '-an -filter:v "select=\'gt(scene, 0.3)\', showinfo" -f null'}
# )
stranger = ffmpy.FFmpeg(
  inputs={"https://archive.org/download/TheStranger_0/The_Stranger.mp4": '-hide_banner'},
  outputs={"pipe:1": '-an -filter:v "select=\'gt(scene, 0.3)\', showinfo" -f null'}
)
stranger.cmd
stdout_stranger, stderr_stranger = stranger.run(
    stdout=subprocess.PIPE, stderr=subprocess.PIPE)

output = stderr_detour.decode("utf-8").split("\n")
filtered_output = list(
    filter(lambda x: "Parsed_showinfo_1" in x and "pts_time" in x, output))
final_output = list(map(lambda y: ((next(filter(lambda z: z.startswith(
    "pts_time"), y.split(" ")), None)).split(":"))[1], filtered_output))
print(final_output)
shot_num = len(final_output)
random_idx = random.randint(0, round(shot_num / 3))
end_tc = round(
    float(final_output[random_idx + random.randint(1, 3)]) - (2 / 29.97), 2)
if float(end_tc) - float(final_output[random_idx]) > 60:
    end_tc = float(final_output[random_idx]) + 60
elif float(end_tc) - float(final_output[random_idx]) < 5:
    end_tc = float(final_output[random_idx]) + 30

output_doa = stderr_doa.decode("utf-8").split("\n")
filtered_output_doa = list(
    filter(lambda x: "Parsed_showinfo_1" in x and "pts_time" in x, output_doa))
final_output_doa = list(map(lambda y: ((next(filter(lambda z: z.startswith(
    "pts_time"), y.split(" ")), None)).split(":"))[1], filtered_output_doa))
print(final_output_doa)
shot_num_doa = len(final_output_doa)
random_idx_doa = random.randint(
    round(shot_num_doa / 3), (round(shot_num_doa / 3) * 2))
end_tc_doa = round(
    float(final_output_doa[random_idx_doa + random.randint(1, 3)]) - (2 / 29.97), 2)
if float(end_tc_doa) - float(final_output_doa[random_idx_doa]) > 60:
    end_tc_doa = float(final_output_doa[random_idx_doa]) + 60
elif float(end_tc_doa) - float(final_output_doa[random_idx_doa]) < 5:
    end_tc_doa = float(final_output_doa[random_idx_doa]) + 30

output_stranger = stderr_stranger.decode("utf-8").split("\n")
filtered_output_stranger = list(
    filter(lambda x: "Parsed_showinfo_1" in x and "pts_time" in x, output_stranger))
final_output_stranger = list(map(lambda y: ((next(filter(lambda z: z.startswith(
    "pts_time"), y.split(" ")), None)).split(":"))[1], filtered_output_stranger))
print(final_output_stranger)
shot_num_stranger = len(final_output_stranger)
random_idx_stranger = random.randint(
    (round(shot_num_stranger / 3) * 2), shot_num_stranger)
end_tc_stranger = round(float(
    final_output_stranger[random_idx_stranger + random.randint(1, 3)]) - (2 / 29.97), 2)
if float(end_tc_stranger) - float(final_output_stranger[random_idx_stranger]) > 60:
    end_tc_stranger = float(final_output_stranger[random_idx_stranger]) + 60
elif float(end_tc_stranger) - float(final_output_stranger[random_idx_stranger]) < 5:
    end_tc_stranger = float(final_output_stranger[random_idx_stranger]) + 30

# ff2_detour = ffmpy.FFmpeg(
#   inputs={"https://archive.org/download/BerlinSymphonyofaGreatCity/BERLIN_512kb.mp4": f'-ss {final_output[random_idx]} -to {end_tc}'},
#   outputs={"test_detour.mp4":None}
# )
# ff2_detour = ffmpy.FFmpeg(
#     inputs={"https://archive.org/download/12AngryMen1957Trailer/12AngryMen1957trailer.mp4":
#             f'-ss {final_output[random_idx]} -to {end_tc}'},
#     outputs={"test_detour.mp4": None}
# )
ff2_detour = ffmpy.FFmpeg(
    inputs={"https://archive.org/download/Detour_movie/Detour.mp4":
            f'-ss {final_output[random_idx]} -to {end_tc}'},
    outputs={"test_detour.mp4": None}
)
ff2_detour.cmd
ff2_detour.run()

# ff2_doa = ffmpy.FFmpeg(
#   inputs={"https://archive.org/download/AliceInWonderland1803/AliceInWonderland1803.mp4": f'-ss {final_output_doa[random_idx_doa]} -to {end_tc_doa}'},
#   outputs={"test_doa.mp4":None}
# )
# ff2_doa = ffmpy.FFmpeg(
#     inputs={"https://archive.org/download/2001ASpaceOdysseyTrailer/2001ASpaceOdysseyTrailer.mp4":
#             f'-ss {final_output_doa[random_idx_doa]} -to {end_tc_doa}'},
#     outputs={"test_doa.mp4": None}
# )
ff2_doa = ffmpy.FFmpeg(
    inputs={"https://archive.org/download/doa_1949/doa_1949.mp4":
            f'-ss {final_output_doa[random_idx_doa]} -to {end_tc_doa}'},
    outputs={"test_doa.mp4": None}
)
ff2_doa.cmd
ff2_doa.run()

# ff2_stranger = ffmpy.FFmpeg(
#   inputs={"https://archive.org/download/20000LeaguesUndertheSea/20000_Leagues_Under_the_Sea_512kb.mp4": f'-ss {final_output_stranger[random_idx_stranger]} -to {end_tc_stranger}'},
#   outputs={"test_stranger.mp4":None}
# )
# ff2_stranger = ffmpy.FFmpeg(
#     inputs={"https://archive.org/download/49thParallelTrailer/49thParallelTrailer.mp4":
#             f'-ss {final_output_stranger[random_idx_stranger]} -to {end_tc_stranger}'},
#     outputs={"test_stranger.mp4": None}
# )
ff2_stranger = ffmpy.FFmpeg(
    inputs={"https://archive.org/download/TheStranger_0/The_Stranger.mp4":
            f'-ss {final_output_stranger[random_idx_stranger]} -to {end_tc_stranger}'},
    outputs={"test_stranger.mp4": None}
)
ff2_stranger.cmd
ff2_stranger.run()

ff3_merge = ffmpy.FFmpeg(
    inputs={"ffmpeg_demuxer_test.txt": "-f concat"},
    outputs={"test_concat.mp4": "-c copy"}
)

ff3_merge.cmd
ff3_merge.run()

files_to_delete = ["test_detour.mp4", "test_doa.mp4", "test_stranger.mp4"]

def clearFiles(files):
    print("start of clearfiles call")
    for file in files:
        print(f"deleting: {file}")
        os.remove(file)
    print("files have been deleted")

timer = Timer(5.0, clearFiles, files_to_delete)

timer.start()

