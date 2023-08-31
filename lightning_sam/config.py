from box import Box

config = {
    "num_devices": 1,
    "batch_size": 4,
    "num_workers": 2,
    "num_epochs": 20,
    "eval_interval": 2,
    "out_dir": "out/training",
    "opt": {
        "learning_rate": 8e-4,
        "weight_decay": 1e-4,
        "decay_factor": 10,
        "steps": [60000, 86666],
        "warmup_steps": 250,
    },
    "model": {
        "type": 'vit_h',
        "checkpoint": "D:\\Code\\lightning-sam\\checkpoints\\checkpoints\\sam_vit_h_4b8939.pth",
        "freeze": {
            "image_encoder": True,
            "prompt_encoder": True,
            "mask_decoder": False,
        },
    },
    "dataset": {
        "train": {
            "root_dir": "D:\\Code\\lightning-sam\\COCO",
            "annotation_file": "D:\\Code\\lightning-sam\\COCO\\train.json"
        },
        "val": {
            "root_dir": "D:\\Code\\lightning-sam\\COCO",
            "annotation_file": "D:\\Code\\lightning-sam\\COCO\\val.json"
        }
    }
}

cfg = Box(config)
