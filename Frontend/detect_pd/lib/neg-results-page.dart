import 'package:detect_pd/settings-page.dart';
import 'package:detect_pd/widgets/navbar.dart';
import 'package:detect_pd/widgets/results-background.dart';
import 'package:detect_pd/widgets/results-foreground.dart';
import 'package:flutter/material.dart';
import 'about-page.dart';
import 'main.dart';

void main() => runApp(MaterialApp(
      home: NegativeResultsPage(),
    ));

class NegativeResultsPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: ResultsForeground(
          mainBackgroundColor: Colors.greenAccent,
          fillColor: Colors.cyan.shade800,
          resultImage: ResultBackground(
            resultBackgroundHeight: 460.0,
            resultBackgroundImage: 'assets/positiveBackground.png',
          ),
          expandedHeight: 300.0,
          result: 'Parkinson\'s Disease \n Not Detected'),
      bottomNavigationBar: NavBar(
        link1: () {
          Navigator.pushReplacement(
              context, MaterialPageRoute(builder: (context) => AboutPDPage()));
        },
        link2: () {
          Navigator.pushReplacement(
              context, MaterialPageRoute(builder: (context) => HomePage()));
        },
        link3: () {
          Navigator.pushReplacement(
              context, MaterialPageRoute(builder: (context) => SettingsPage()));
        },
        backgroundColor: Color.fromRGBO(240, 241, 226, 100),
      ),
    );
  }
}
