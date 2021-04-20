import 'package:url_launcher/url_launcher.dart';

// method for calling async function
launcher(){
  launchURL();
}

// async function to redirect user to web page
launchURL() async {
  const url = 'http://detectpd.us-east-2.elasticbeanstalk.com';
  if (await canLaunch(url)) {
    await launch(url);
  } else {
    throw 'Could not launch $url';
  }
}