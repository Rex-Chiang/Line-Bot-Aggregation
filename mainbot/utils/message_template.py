from django.conf import settings

def vocabulary_card(vocabulary_list, example, translation):
    return {
        "type": "bubble",
        "hero": {
            "type": "image",
            "url": settings.MESSAGE_PICTURE_URL,
            "size": "full",
            "aspectRatio": "32:15",
            "aspectMode": "cover"
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                        {
                            "type": "text",
                            "text": "Vocabulary 1 : ",
                            "color": "#aaaaaa",
                            "size": "lg",
                            "flex": 6
                        },
                        {
                            "type": "text",
                            "text": vocabulary_list[0][0],
                            "wrap": True,
                            "color": "#666666",
                            "size": "lg",
                            "flex": 6
                        }
                    ],
                    "margin": "md"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                        {
                            "type": "text",
                            "text": "Chinese : ",
                            "color": "#aaaaaa",
                            "size": "lg",
                            "flex": 6
                        },
                        {
                            "type": "text",
                            "text": vocabulary_list[0][1],
                            "wrap": True,
                            "color": "#666666",
                            "size": "lg",
                            "flex": 6
                        }
                    ],
                    "margin": "md"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                        {
                            "type": "text",
                            "text": "Vocabulary 2 : ",
                            "color": "#aaaaaa",
                            "size": "lg",
                            "flex": 6
                        },
                        {
                            "type": "text",
                            "text": vocabulary_list[1][0],
                            "wrap": True,
                            "color": "#666666",
                            "size": "lg",
                            "flex": 6
                        }
                    ],
                    "margin": "md"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                        {
                            "type": "text",
                            "text": "Chinese : ",
                            "color": "#aaaaaa",
                            "size": "lg",
                            "flex": 6
                        },
                        {
                            "type": "text",
                            "text": vocabulary_list[1][1],
                            "wrap": True,
                            "color": "#666666",
                            "size": "lg",
                            "flex": 6
                        }
                    ],
                    "margin": "md"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                        {
                            "type": "text",
                            "text": "Vocabulary 3 : ",
                            "color": "#aaaaaa",
                            "size": "lg",
                            "flex": 6
                        },
                        {
                            "type": "text",
                            "text": vocabulary_list[2][0],
                            "wrap": True,
                            "color": "#666666",
                            "size": "lg",
                            "flex": 6
                        }
                    ],
                    "margin": "md"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                        {
                            "type": "text",
                            "text": "Chinese : ",
                            "color": "#aaaaaa",
                            "size": "lg",
                            "flex": 6
                        },
                        {
                            "type": "text",
                            "text": vocabulary_list[2][1],
                            "wrap": True,
                            "color": "#666666",
                            "size": "lg",
                            "flex": 6
                        }
                    ],
                    "margin": "md"
                }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "spacing": "md",
            "contents": [
                {
                    "type": "text",
                    "text": "Example",
                    "color": "#aaaaaa",
                    "size": "lg",
                    "align": "center"
                },
                {
                    "type": "text",
                    "text": example,
                    "wrap": True,
                    "color": "#666666",
                    "size": "md"
                },
                {
                    "type": "text",
                    "text": translation,
                    "wrap": True,
                    "color": "#aaaaaa",
                    "size": "md"
                }
            ]
        }
    }