
// Load the Visualization API and the piechart package.
google.load('visualization', '1', {
    packages: ['corechart'],
});

// Set a callback to run when the Google Visualization API is loaded.
google.setOnLoadCallback(hashtagChart);

google.setOnLoadCallback(messageChart);

google.setOnLoadCallback(replyChart);

google.setOnLoadCallback(likeChart);

google.setOnLoadCallback(dislikeChart);

function reformatData(jsonData){
    var temp= jsonData.Result;
    console.log("temp: " + JSON.stringify(temp));
    var result = [];
    var i;
    var row;
    for (i=0; i < temp.length; ++i){
        row= temp[i];
        dataElement = [];
        dataElement.push(row.info);
        dataElement.push(row.count);
        result.push(dataElement);
    }
    console.log("Data: " + JSON.stringify(result));
    return result;
}

function hashtagChart() {
    var jsonData = $.ajax({
        url: "http://localhost:5000/PhotoMessagingApp/dashboard/trending",
        dataType: "json",
        async: false
    }).responseText;

    console.log("jsonData: " + JSON.parse(jsonData));

    // Create our data table out of JSON data loaded from server.
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Hashtag');
    data.addColumn('number', 'Tags');
    data.addRows(reformatData(JSON.parse(jsonData)));

    var options = {
        title: 'Trending Topics',
        width: 600,
        height: 450,
        chartArea: {width: '60%'},
        hAxis: {
            title: 'Hashtag',
            minValue: 0
        },
        vAxis: {
            title: 'Messages Tagged'
        },
        colors:['#8a63cc']
    };

    var chart = new google.visualization.ColumnChart(document.getElementById('hashtag_chart_div'));
    chart.draw(data, options);
}

function messageChart() {
    var jsonData = $.ajax({
        url: "http://localhost:5000/PhotoMessagingApp/dashboard/posts",
        dataType: "json",
        async: false
    }).responseText;

    console.log("jsonData: " + JSON.parse(jsonData));

    // Create our data table out of JSON data loaded from server.
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Date');
    data.addColumn('number', 'Messages');
    data.addRows(reformatData(JSON.parse(jsonData)));

    var options = {
        title: 'Messages Per Day',
        width: 600,
        height: 450,
        chartArea: {width: '60%'},
        color: 'red',
        hAxis: {
            title: 'Date',
            minValue: 0
        },
        vAxis: {
            title: 'Total Messages Posted'
        },
        colors:['#ffa500']
    };

    var chart = new google.visualization.ColumnChart(document.getElementById('message_chart_div'));
    chart.draw(data, options);
}

function replyChart() {
    var jsonData = $.ajax({
        url: "http://localhost:5000/PhotoMessagingApp/dashboard/replies",
        dataType: "json",
        async: false
    }).responseText;

    console.log("jsonData: " + JSON.parse(jsonData));

    // Create our data table out of JSON data loaded from server.
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Date');
    data.addColumn('number', 'Replies');
    data.addRows(reformatData(JSON.parse(jsonData)));

    var options = {
        title: 'Replies Per Day',
        width: 600,
        height: 450,
        chartArea: {width: '60%'},
        hAxis: {
            title: 'Date',
            minValue: 0
        },
        vAxis: {
            title: 'Total Replies'
        },
        colors:['#cccc11']
    };

    var chart = new google.visualization.ColumnChart(document.getElementById('reply_chart_div'));
    chart.draw(data, options);
}

function likeChart() {
    var jsonData = $.ajax({
        url: "http://localhost:5000/PhotoMessagingApp/dashboard/likes",
        dataType: "json",
        async: false
    }).responseText;

    console.log("jsonData: " + JSON.parse(jsonData));

    // Create our data table out of JSON data loaded from server.
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Date');
    data.addColumn('number', 'Likes');
    data.addRows(reformatData(JSON.parse(jsonData)));

    var options = {
        title: 'Likes Per Day',
        width: 600,
        height: 450,
        chartArea: {width: '60%'},
        hAxis: {
            title: 'Date',
            minValue: 0
        },
        vAxis: {
            title: 'Total Likes'
        },
        colors:['#5acc48']
    };

    var chart = new google.visualization.ColumnChart(document.getElementById('like_chart_div'));
    chart.draw(data, options);
}

function dislikeChart() {
    var jsonData = $.ajax({
        url: "http://localhost:5000/PhotoMessagingApp/dashboard/dislikes",
        dataType: "json",
        async: false
    }).responseText;

    console.log("jsonData: " + JSON.parse(jsonData));

    // Create our data table out of JSON data loaded from server.
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Date');
    data.addColumn('number', 'Dislikes');
    data.addRows(reformatData(JSON.parse(jsonData)));

    var options = {
        title: 'Dislikes Per Day',
        width: 600,
        height: 450,
        chartArea: {width: '60%'},
        hAxis: {
            title: 'Date',
            minValue: 0
        },
        vAxis: {
            title: 'Total Dislikes'
        },
        colors:['#cc3e47']
    };

    var chart = new google.visualization.ColumnChart(document.getElementById('dislike_chart_div'));
    chart.draw(data, options);
}



