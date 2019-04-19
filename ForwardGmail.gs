function myFunction() {
  var threads = GmailApp.search("in:Transactions");
  Logger.log(threads);
  for (var i = 0; i < threads.length; i++) {
    // logic of calling lambda API endpoint with message
  }
}
