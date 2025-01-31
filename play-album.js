const fs = require("fs/promises");
const play = require("./song-player");

async function getAlbumData(albumName){
    try {
        const albumData = await fs.readFile(`${albumName}.json`, "utf-8");
        return JSON.parse(albumData);
    } catch(err) {
        return "404: Album not found";
    }
}

getAlbumData("neural-anthems").then((album) => {
    play(album);
})