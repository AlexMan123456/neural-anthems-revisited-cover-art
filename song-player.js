function play(music){
    console.log(`Now playing ${music.title} by ${music.artist}`);
    const {songs} = music;
    console.log()
    console.log("Songs to play:")
    for(const song of songs){
        console.log(`   ${song.title} by ${song.artist} ft. ${song.featuringArtists.join(", ")}`)
    }
}

module.exports = play