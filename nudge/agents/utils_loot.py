import numpy as np
import torch

device = torch.device('cuda:0')


def simplify_action_loot(action):
    """simplify 9 actions to 5 actions
    """
    #          left,down,idle,up,right
    # model_ouput  [0, 1, 2, 3, 4]
    action_space = [1, 3, 4, 5, 7]
    action = action_space[action]
    return np.array([action])


def preds_to_action_loot(action, prednames):
    """
    map explaining to action
    action_space = [1, 3, 4, 5, 7]
    """
    if 'up' in prednames[action]:
        return np.array([5])
    elif 'down' in prednames[action]:
        return np.array([3])
    elif 'left' in prednames[action]:
        return np.array([1])
    elif 'right' in prednames[action]:
        return np.array([7])
    elif 'idle' in prednames[action]:
        return np.array([4])


def action_map_loot(prediction, args, prednames=None):
    """map model action to game action"""
    if args.alg == 'ppo':
        action = simplify_action_loot(prediction)
    elif args.alg == 'logic':
        action = preds_to_action_loot(prediction, prednames)
    return action
