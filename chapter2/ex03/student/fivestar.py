new_video = 3.00
old_video = 2.00

num_new_videos = int(input("Enter the number of new videos: "))
num_old_videos = int(input("Enter the number of old videos: "))

total_cost = (num_new_videos * new_video) + (num_old_videos * old_video)

print(f"The total cost is ${total_cost:.2f}")