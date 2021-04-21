import 'package:url_launcher/url_launcher.dart';

// method for calling async function
launcher(){
  launchURL();
}

// async function to redirect user to web page
launchURL() async {
  const url = 'https://bawanthaperera1999.wixsite.com/website';
  if (await canLaunch(url)) {
    await launch(url);
  } else {
    throw 'Could not launch $url';
  }
}