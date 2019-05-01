function myFunction() {
  var threads = GmailApp.search("in:Transactions"); // search for messages with the label Transactions
  for (var i = 0; i < threads.length; i++) {
     var messages = threads[i].getMessages();
     for (var m = 0; m < messages.length; m++) {
       var msg = messages[m].getPlainBody();

       Logger.log(msg);

     }
  }
}

