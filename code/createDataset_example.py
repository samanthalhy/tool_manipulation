# example of the dataset generation

import csv
import random

header = ['prompt', 'completion']
all_data = []
data = []

def robotPose():
    robot_y = round(random.randint(250, 300))
    left = [round(random.randint(160, 200)), robot_y]
    right = [round(random.randint(390, 430)), robot_y]
    return left, right

def singleToolPose(tool_id):
    diff = round(random.randint(3, 10))
    if tool_id == 0:
        # tool = 'stick'
        tool_keypoints = [[round(random.randint(320 - diff, 320 + diff)), round(random.randint(170 - diff, 170 + diff))],
                          [round(random.randint(320 - diff, 320 + diff)), round(random.randint(240 - diff, 240 + diff))]]
        tool_pose = tool_keypoints[-1]
    elif tool_id == 1:
        # tool = 'hook'
        tool_keypoints = [[round(random.randint(290 - diff, 290 + diff)), round(random.randint(170 - diff, 170 + diff))],
                          [round(random.randint(330 - diff, 330 + diff)), round(random.randint(170 - diff, 170 + diff))],
                          [round(random.randint(330 - diff, 330 + diff)), round(random.randint(240 - diff, 240 + diff))]]
        tool_pose = tool_keypoints[-1]
    else:
        # tool = 'y-hook'
        tool_keypoints = [[round(random.randint(290 - diff, 290 + diff)), round(random.randint(180 - diff, 180 + diff))],
                          [round(random.randint(340 - diff, 340 + diff)), round(random.randint(180 - diff, 180 + diff))],
                          [round(random.randint(310 - diff, 310 + diff)), round(random.randint(210 - diff, 210 + diff))],
                          [round(random.randint(310 - diff, 310 + diff)), round(random.randint(240 - diff, 240 + diff))]]
        tool_pose = tool_keypoints[-1]
    return tool_keypoints, tool_pose

def multiToolPose(tool_id):
    diff = round(random.randint(0, 10))
    stick_right = [[round(random.randint(350 - diff, 350 + diff)), round(random.randint(170 - diff, 170 + diff))],
                   [round(random.randint(350 - diff, 350 + diff)), round(random.randint(240 - diff, 240 + diff))]]
    stick_left = [[round(random.randint(290 - diff, 290 + diff)), round(random.randint(170 - diff, 170 + diff))],
                  [round(random.randint(290 - diff, 290 + diff)), round(random.randint(240 - diff, 240 + diff))]]

    hook_right = [[round(random.randint(350 - diff, 350 + diff)), round(random.randint(170 - diff, 170 + diff))],
                  [round(random.randint(420 - diff, 420 + diff)), round(random.randint(170 - diff, 170 + diff))],
                  [round(random.randint(420 - diff, 420 + diff)), round(random.randint(240 - diff, 240 + diff))]]
    hook_left = [[round(random.randint(250 - diff, 250 + diff)), round(random.randint(190 - diff, 190 + diff))],
                 [round(random.randint(300 - diff, 300 + diff)), round(random.randint(190 - diff, 190 + diff))],
                 [round(random.randint(300 - diff, 300 + diff)), round(random.randint(240 - diff, 240 + diff))]]

    y_hook_right = [[round(random.randint(300 - diff, 300 + diff)), round(random.randint(180 - diff, 180 + diff))],
                    [round(random.randint(360 - diff, 360 + diff)), round(random.randint(180 - diff, 180 + diff))],
                    [round(random.randint(330 - diff, 330 + diff)), round(random.randint(210 - diff, 210 + diff))],
                    [round(random.randint(330 - diff, 330 + diff)), round(random.randint(240 - diff, 240 + diff))]]
    y_hook_left = [[round(random.randint(250 - diff, 250 + diff)), round(random.randint(180 - diff, 180 + diff))],
                   [round(random.randint(300 - diff, 300 + diff)), round(random.randint(180 - diff, 180 + diff))],
                   [round(random.randint(275 - diff, 275 + diff)), round(random.randint(210 - diff, 210 + diff))],
                   [round(random.randint(275 - diff, 275 + diff)), round(random.randint(240 - diff, 240 + diff))]]

    # tool's combination
    if tool_id == 0:
        # tool = 'stick y-hook'
        tool_keypoints = [stick_left, y_hook_right]
        tool_pose = [stick_left[-1], y_hook_right[-1]]
    elif tool_id == 1:
        # tool = 'y-hook stick'
        tool_keypoints = [y_hook_left, stick_right]
        tool_pose = [y_hook_left[-1], stick_right[-1]]
    elif tool_id == 2:
        # tool = 'stick hook'
        tool_keypoints = [stick_left, hook_right]
        tool_pose = [stick_left[-1], hook_right[-1]]
    elif tool_id == 3:
        # tool = 'hook stick'
        tool_keypoints = [hook_left, stick_right]
        tool_pose = [hook_left[-1], stick_right[-1]]
    elif tool_id == 4:
        # tool = 'y-hook hook'
        tool_keypoints = [y_hook_left, hook_right]
        tool_pose = [y_hook_left[-1], hook_right[-1]]
    else:
        # tool = 'hook y-hook'
        tool_keypoints = [hook_left, y_hook_right]
        tool_pose = [hook_left[-1], y_hook_right[-1]]
    return tool_keypoints, tool_pose

def singleBlockTargetPose(side):
    if side == 0:
        # right single
        block = [round(random.randint(320, 540)), round(random.randint(80, 250))]
        target = [round(random.randint(320, 540)), round(random.randint(80, 250))]
    else:
        # left single
        block = [round(random.randint(110, 320)), round(random.randint(80, 250))]
        target = [round(random.randint(110, 320)), round(random.randint(80, 250))]
    return block, target

def dualBlockTargetPose(side):
    if side == 0:
        # right to left
        block = [round(random.randint(320, 540)), round(random.randint(80, 250))]
        target = [round(random.randint(110, 320)), round(random.randint(80, 250))]
    else:
        # left to right
        block = [round(random.randint(110, 320)), round(random.randint(80, 250))]
        target = [round(random.randint(320, 540)), round(random.randint(80, 250))]
    return block, target

def singleSingleTool():
    # single robot, single tool
    for i in range(1):
        left, right = robotPose()
        side = round(random.randint(0, 1))
        block, target = singleBlockTargetPose(side)

        while block == target:
            target = [target[0] + 6, target[1] + 6]

        taskList = ['Move the block to target with tool', 'Push the block to the target']
        task = taskList[round(random.randint(0, 1))]

        tool_id = round(random.randint(0, 2))

        # single
        tool_keypoints, tool_pose = singleToolPose(tool_id)

        wall = 'False'
        prompt_str = str(task) + ';leftRobot:' + str(left) + ';rightRobot:' + str(right) + ';toolPose:' + str(tool_pose) + ';toolKeypoints:' + str(tool_keypoints) + ';block current:' + str(block) + ';block target:' + str(target) + ';wall:' + str(wall) + ';'

        if side == 0:
            # right single
            if tool_id == 0:
                step = 'grasp(right, stick); approach(right, stick, block); interact(right, stick, block, target); release(right, stick);'
            elif tool_id == 1:
                step = 'grasp(right, hook); approach(right, hook, block); interact(right, hook, block, target); release(right, hook);'
            else:
                step = 'grasp(right, y-hook); approach(right, y-hook, block); interact(right, y-hook, block, target); release(right, y-hook);'

        else:
            # left single
            if tool_id == 0:
                step = 'grasp(left, stick); approach(left, stick, block); interact(left, stick, block, target); release(left, stick);'
            elif tool_id == 1:
                step = 'grasp(left, hook); approach(left, hook, block); interact(left, hook, block, target); release(left, hook);'
            else:
                step = 'grasp(left, y-hook); approach(left, y-hook, block); interact(left, y-hook, block, target); release(left, y-hook);'


        data = [prompt_str, str(step)]
        all_data.append(data)

def singleMultiTool():
    #### single robot, multi-tool
    for i in range(1):
        left, right = robotPose()
        side = round(random.randint(0, 1))
        block, target = singleBlockTargetPose(side)

        while block == target:
            target = [target[0] + 6, target[1] + 6]

        taskList = ['Move the block to target with tool', 'Push the block to the target']
        task = taskList[round(random.randint(0, 1))]

        tool_id = round(random.randint(0, 5))

        tool_keypoints, tool_pose = multiToolPose(tool_id)

        wall = 'False'
        prompt_str = str(task) + ';leftRobot:' + str(left) + ';rightRobot:' + str(right) + ';toolPose:' + str(tool_pose) + ';toolKeypoints:' + str(tool_keypoints) + ';block current:' + str(block) + ';block target:' + str(target) + ';wall:' + str(wall) + ';'


        if side == 0:
            # right single
            if tool_id == 0 or tool_id == 1 or tool_id == 5:
                step = 'grasp(right, y-hook); approach(right, y-hook, block); interact(right, y-hook, block, target); release(right, y-hook);'
            elif tool_id == 2 or tool_id == 3 or tool_id == 4:
                step = 'grasp(right, hook); approach(right, hook, block); interact(right, hook, block, target); release(right, hook);'


        if side == 1:
            # left single
            if tool_id == 0 or tool_id == 1 or tool_id == 4:
                step = 'grasp(left, y-hook); approach(left, y-hook, block); interact(left, y-hook, block, target); release(left, y-hook);'
            elif tool_id == 2 or tool_id == 3 or tool_id == 5:
                step = 'grasp(left, hook); approach(left, hook, block); interact(left, hook, block, target); release(left, hook);'


        data = [prompt_str, str(step)]
        all_data.append(data)

def sharing():
    # single robot, single tool, sharing
    for i in range(1):
        left, right = robotPose()
        side = round(random.randint(0, 1))
        block, target = dualBlockTargetPose(side)

        while block == target:
            target = [target[0] + 6, target[1] + 6]

        taskList = ['Move the block to target with tool', 'Push the block to the target']
        task = taskList[round(random.randint(0, 1))]

        tool_id = round(random.randint(0, 2))

        # single
        tool_keypoints, tool_pose = singleToolPose(tool_id)

        wall = 'False'
        prompt_str = str(task) + ';leftRobot:' + str(left) + ';rightRobot:' + str(right) + ';toolPose:' + str(tool_pose) + ';toolKeypoints:' + str(tool_keypoints) + ';block current:' + str(block) + ';block target:' + str(target) + ';wall:' + str(wall) + ';'


        if side == 0:
            # right single
            if tool_id == 0:
                step = 'grasp(right, stick); approach(right, stick, block); interact(right, stick, block, goal); pass(right, stick, block, left); release(right, stick); grasp(left, stick); approach(left, stick, block); interact(left, stick, block, target); release(left, stick);'
            elif tool_id == 1:
                step = 'grasp(right, hook); approach(right, hook, block); interact(right, hook, block, goal); pass(right, hook, block, left); release(right, hook); grasp(left, hook); approach(left, hook, block); interact(left, hook, block, target); release(left, hook);'
            else:
                step = 'grasp(right, y-hook); approach(right, y-hook, block); interact(right, y-hook, block, goal); pass(right, y-hook, block, left); release(right, y-hook); grasp(left, y-hook); approach(left, y-hook, block); interact(left, y-hook, block, target); release(left, y-hook);'

        else:
            # left single
            if tool_id == 0:
                step = 'grasp(left, stick); approach(left, stick, block); interact(left, stick, block, goal); pass(left, stick, block, right); release(left, stick); grasp(right, stick); approach(right, stick, block); interact(right, stick, block, target); release(right, stick);'
            elif tool_id == 1:
                step = 'grasp(left, hook); approach(left, hook, block); interact(left, hook, block, goal); pass(left, hook, block, right); release(left, hook); grasp(right, hook); approach(right, hook, block); interact(right, hook, block, target); release(right, hook);'
            else:
                step = 'grasp(left, y-hook); approach(left, y-hook, block); interact(left, y-hook, block, goal); pass(left, y-hook, block, right); release(left, y-hook); grasp(right, y-hook); approach(right, y-hook, block); interact(right, y-hook, block, target); release(right, y-hook);'


        data = [prompt_str, str(step)]
        all_data.append(data)

def long():
    # single robot, multi tool, long horizon
    for i in range(1):
        left, right = robotPose()
        side = round(random.randint(0, 1))
        block, target = dualBlockTargetPose(side)

        while block == target:
            target = [target[0] + 6, target[1] + 6]

        taskList = ['Move the block to target with tool', 'Push the block to the target']
        task = taskList[round(random.randint(0, 1))]

        tool_id = round(random.randint(0, 5))

        tool_keypoints, tool_pose = multiToolPose(tool_id)

        wall = 'False'
        prompt_str = str(task) + ';leftRobot:' + str(left) + ';rightRobot:' + str(right) + ';toolPose:' + str(tool_pose) + ';toolKeypoints:' + str(tool_keypoints) + ';block current:' + str(block) + ';block target:' + str(target) + ';wall:' + str(wall) + ';'


        if side == 0:
            # right first
            if tool_id == 0:
                step = 'grasp(right, y-hook); grasp(left, stick); approach(right, y-hook, block); interact(right, y-hook, block, goal); pass(right, y-hook, block, left); approach(left, stick, block); interact(left, stick, block, target); release(right, y-hook); release(left, stick);'
            elif tool_id == 1:
                step = 'grasp(right, stick); grasp(left, y-hook); approach(right, stick, block); interact(right, stick, block, goal); pass(right, stick, block, left); approach(left, y-hook, block); interact(left, y-hook, block, target); release(right, stick); release(left, y-hook);'
            elif tool_id == 2:
                step = 'grasp(right, hook); grasp(left, stick); approach(right, hook, block); interact(right, hook, block, goal); pass(right, hook, block, left); approach(left, stick, block); interact(left, stick, block, target); release(right, hook); release(left, stick);'
            elif tool_id == 3:
                step = 'grasp(right, stick); grasp(left, hook); approach(right, stick, block); interact(right, stick, block, goal); pass(right, stick, block, left); approach(left, hook, block); interact(left, hook, block, target); release(right, stick); release(left, hook);'
            elif tool_id == 4:
                step = 'grasp(right, hook); grasp(left, y-hook); approach(right, hook, block); interact(right, hook, block, goal); pass(right, hook, block, left); approach(left, y-hook, block); interact(left, y-hook block, target); release(right, hook); release(left, y-hook);'
            elif tool_id == 5:
                step = 'grasp(right, y-hook); grasp(left, hook); approach(right, y-hook, block); interact(right, y-hook, block, goal); pass(right, y-hook, block, left); approach(left, hook, block); interact(left, hook, block, target); release(right, y-hook); release(left, hook);'

        else:
            # left first
            if tool_id == 0:
                step = 'grasp(left, stick); grasp(right, y-hook); approach(left, stick, block); interact(left, stick, block, goal); pass(left, stick, block, right); approach(right, y-hook, block); interact(right, y-hook, block, target); release(left, stick); release(right, y-hook);'
            elif tool_id == 1:
                step = 'grasp(left, y-hook); grasp(right, stick); approach(left, y-hook, block); interact(left, y-hook, block, goal); pass(left, y-hook, block, right); approach(right, stick, block); interact(right, stick, block, target); release(left, y-hook); release(right, stick);'
            elif tool_id == 2:
                step = 'grasp(left, stick); grasp(right, hook); approach(left, stick, block); interact(left, stick, block, goal); pass(left, stick, block, right); approach(right, hook, block); interact(right, hook, block, target); release(left, stick); release(right, hook);'
            elif tool_id == 3:
                step = 'grasp(left, hook); grasp(right, stick); approach(left, hook, block); interact(left, hook, block, goal); pass(left, hook, block, right); approach(right, stick, block); interact(right, stick, block, target); release(left, hook); release(right, stick);'
            elif tool_id == 4:
                step = 'grasp(left, y-hook); grasp(right, hook); approach(left, y-hook, block); interact(left, y-hook, block, goal); pass(left, y-hook, block, right); approach(right, hook, block); interact(right, hook, block, target); release(left, y-hook); release(right, hook);'
            elif tool_id == 5:
                step = 'grasp(left, hook); grasp(right, y-hook); approach(left, hook, block); interact(left, hook, block, goal); pass(left, hook, block, right); approach(right, y-hook, block); interact(right, y-hook, block, target); release(left, hook); release(right, y-hook);'


        data = [prompt_str, str(step)]
        all_data.append(data)

def wall():
    # single robot, single tool, wall
    for i in range(1):
        left, right = robotPose()
        side = round(random.randint(0, 1))

        taskList = ['Move the block out with tool', 'Get the block out', 'Get the block out from the walls']
        task = taskList[round(random.randint(0, 2))]

        tool_id = round(random.randint(0, 2))

        # single
        tool_keypoints, tool_pose = singleToolPose(tool_id)

        wall = 'True'

        wall_id = round(random.randint(0, 2))

        diff = round(random.randint(0, 3))
        if side == 0:
            if wall_id == 0:
                fourPt = [[440, 160], [390, 160], [390, 230], [440, 230]]   # c shape
            elif wall_id == 1:
                fourPt = [[430, 150], [390, 170], [390, 220], [430, 240]]
            elif wall_id == 2:
                fourPt = [[480, 170], [480, 110], [400, 110], [400, 170]]   # n shape
        if side == 1:
            if wall_id == 0:
                fourPt = [[210, 160], [160, 160], [160, 230], [210, 230]]
            elif wall_id == 1:
                fourPt = [[190, 150], [160, 160], [160, 200], [190, 220]]
            elif wall_id == 2:
                fourPt = [[210, 160], [210, 130], [140, 140], [140, 174]]

        wall_keypoints = [[round(random.randint(fourPt[0][0] - diff, fourPt[0][0] + diff)), round(random.randint(fourPt[0][1] - diff, fourPt[0][1] + diff))],
                          [round(random.randint(fourPt[1][0] - diff, fourPt[1][0] + diff)), round(random.randint(fourPt[1][1] - diff, fourPt[1][1] + diff))],
                          [round(random.randint(fourPt[2][0] - diff, fourPt[2][0] + diff)), round(random.randint(fourPt[2][1] - diff, fourPt[2][1] + diff))],
                          [round(random.randint(fourPt[3][0] - diff, fourPt[3][0] + diff)), round(random.randint(fourPt[3][1] - diff, fourPt[3][1] + diff))]]

        x = [p[0] for p in wall_keypoints]
        y = [p[1] for p in wall_keypoints]
        block = (int(sum(x) / len(wall_keypoints)), int(sum(y) / len(wall_keypoints)))

        prompt_str = str(task) + ';leftRobot:' + str(left) + ';rightRobot:' + str(right) + ';toolPose:' + str(tool_pose) + ';toolKeypoints:' + str(tool_keypoints) + ';block current:' + str(block) + ';block target:out;' + 'wall:' + str(wall) + ';wallKeypoints:' + str(wall_keypoints) + ';'

        if side == 0:
            # right single
            if tool_id == 0:
                step = 'grasp(right, stick); approach(right, stick, wall); stepping(right, stick, block); release(right, stick);'
            elif tool_id == 1:
                step = 'grasp(right, hook); approach(right, hook, wall); stepping(right, hook, block); release(right, hook);'
            else:
                step = 'grasp(right, y-hook); approach(right, y-hook, wall); stepping(right, y-hook, block); release(right, y-hook);'

        else:
            # left single
            if tool_id == 0:
                step = 'grasp(left, stick); approach(left, stick, wall); stepping(left, stick, block); release(left, stick);'
            elif tool_id == 1:
                step = 'grasp(left, hook); approach(left, hook, wall); stepping(left, hook, block); release(left, hook);'
            else:
                step = 'grasp(left, y-hook); approach(left, y-hook, wall); stepping(left, y-hook, block); release(left, y-hook);'

        data = [prompt_str, str(step)]
        all_data.append(data)


for i in range(1000):
    luckyDraw = round(random.randint(0, 4))
    if luckyDraw == 0:
        singleSingleTool()
    elif luckyDraw == 1:
        singleMultiTool()
    elif luckyDraw == 2:
        sharing()
    elif luckyDraw == 3:
        long()
    else:
        wall()



with open('dataset_example.csv', 'x', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(all_data)
