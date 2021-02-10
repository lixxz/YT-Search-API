# YouTube Search API

Provides search functionality over latest YouTube videos.

## Setting up
1. Clone the repository:
    ```
    git clone https://github.com/lixxz/YT-Search-API.git
    cd YT-Search-API/
    ```

2. Update the environment variables in *.env.yt_api*. 
    - *API_YT_DEV_KEYS* is cricitcal for app's functionality. You can add multiple API keys like this:
        ```
        API_YT_DEV_KEYS=<key1> <key2>
        ```
    - *API_FETCH_INTERVAL(seconds)* controls how frequently YouTube API is called. Set it to around 300 for testing purpose.

3. Build the images and run the containers:
    ```
    docker-compose up -d --build
    ```

4. API's should be live at http://localhost:8000/api. Wait some time(i.e *API_FETCH_INTERVAL*) for data to be populated.

## API's
1. `search`
    ```
    $ curl "http://localhost:8000/api/search?q=official&page=2"
    {
        "total_results":28,
        "max_results_per_page":10,
        "next_page":3,
        "previous_page":1,
        "results":[
            {
            "video_id":"54encSDmkQU",
            "title":"\u1791\u17b9\u1780\u1797\u17d2\u1793\u17c2\u1780\u17a0\u17bc\u179a\u178f\u17be\u1798\u1780\u1796\u17b8\u17a2\u17d2\u179c\u17b8\ud83d\ude14\ud83d\udc94...BoY LoY Official",
            "description":"",
            "thumbnail_default_url":"https://i.ytimg.com/vi/54encSDmkQU/default.jpg",
            "published_at":"2021-02-10T10:08:34Z"
            },
            {
            "video_id":"UYNWIHeIivA",
            "title":"Mehandi Laga Ke Rakhna 3|New Bhojpuri Movie|Official Full HD Movie 2020 |Khesari Lal Yadav, Amrapali",
            "description":"Mehandi Laga Ke Rakhna 3|New Bhojpuri Movie|Official Full HD Movie 2020 |Khesari Lal Yadav, Amrapali Mehandi Laga Ke Rakhna 3|New Bhojpuri ...",
            "thumbnail_default_url":"https://i.ytimg.com/vi/UYNWIHeIivA/default_live.jpg",
            "published_at":"2021-02-10T10:02:36Z"
            },
            ...
        ]
    }
    ```

2. `latest`
    ```
    $ curl "http://localhost:8000/api/latest"
    {
        "total_results":93,
        "max_results_per_page":10,
        "next_page":2,
        "previous_page":null,
        "results":[
            {
            "video_id":"YzTNvEU8Hio",
            "title":"LIL MAXIMUS, official music video [remember me]",
            "description":"official Musik video by LIL MAXIMUS wrote by maximus singer: maximus btw this is one of my oldest Songs i had on my phone lol.",
            "thumbnail_default_url":"https://i.ytimg.com/vi/YzTNvEU8Hio/default.jpg",
            "published_at":"2021-02-10T10:22:51Z"
            },
            {
            "video_id":"dFNLSsmvTks",
            "title":"The official 888 SMP",
            "description":"Www.youtube.com/888_gaming.",
            "thumbnail_default_url":"https://i.ytimg.com/vi/dFNLSsmvTks/default.jpg",
            "published_at":"2021-02-10T10:20:04Z"
            },
            {
            "video_id":"Bm5uKEUUwmQ",
            "title":"love cricket",
            "description":"",
            "thumbnail_default_url":"https://i.ytimg.com/vi/Bm5uKEUUwmQ/default.jpg",
            "published_at":"2021-02-10T10:16:01Z"
            },
            ...
        ]
    }