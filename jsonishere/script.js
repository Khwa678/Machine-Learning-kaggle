function executeCommand(reqString, dbBaseUrl, apiEndPointUrl) {
    var url = dbBaseUrl + apiEndPointUrl;

    var jsonObj = {
        reqString: reqString
    };

    $.post(url, JSON.stringify(jsonObj), function(result) {
        console.log(result);
    }).fail(function(result) {
        console.log(result);
    });
}