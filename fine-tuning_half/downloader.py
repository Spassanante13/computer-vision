from SoccerNet.Downloader import SoccerNetDownloader

downloader = SoccerNetDownloader(LocalDirectory="path/to/SoccerNet")
downloader.downloadDataTask(task="tracking", split=["train","test"])
