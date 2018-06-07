function updateScoreboard() {
    $.get(scoreboard_path, function(response) {
        let data = "";
        for (let team of response) {
            data += '<div class="team"><div class="team-score">' + team[2] + '</div>' +
                '<div class="team-name">' + team[0] + '</div>' +
                '<div class="meta">'+ team[1] + '</div></div>';
        }
        $('.results-place').html(data);
    });
    setTimeout(updateScoreboard, 10000);
}

$(document).ready(function() {
    updateScoreboard();
});