from yorks_yt_concate.pipeline.steps.get_video_list import GetVideoList
from yorks_yt_concate.pipeline.steps.setp import StepException
from yorks_yt_concate.pipeline.pipiline import Pipeline

CHANNEL_ID = 'UCjXfkj5iapKHJrhYfAF9ZGg'


def main():
    inputs = {
        'channel_id': CHANNEL_ID
    }
    stats = [
        GetVideoList(),

    ]

    p = Pipeline(stats)
    p.run(inputs)


if __name__ == '__main__':
    main()
