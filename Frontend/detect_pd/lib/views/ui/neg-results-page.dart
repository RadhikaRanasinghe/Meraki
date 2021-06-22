import 'package:detect_pd/views/widgets/results-background.dart';
import 'package:detect_pd/views/widgets/results-foreground.dart';
import 'package:flutter/material.dart';

void main() {
  runApp(MaterialApp(

    initialRoute:'load' ,
    routes:{
      'load':(context) =>NegativeResultsPage(),
    },
    debugShowCheckedModeBanner: false,
  )); // MaterialApp
}

class NegativeResultsPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.transparent,
      // building the negative result page body
      body: ResultsForeground(
          mainBackgroundColor: Colors.cyan.shade800,
          fillColor: Colors.transparent,
          foregroundColor: Colors.cyan.shade800,
          borderColor: Colors.cyan.shade800,
          resultImage: ResultBackground(
            resultBackgroundHeight: 500.0,
            resultBackgroundImage: 'assets/positiveBackground.png',
            resultsBackgroundCornerRadius: const Radius.circular(40.0),
          ), //ResultBackground
          expandedHeight: 300.0,
          result: 'Parkinson\'s Disease \n Not Detected'), //ResultsForeground
    ); //Scaffold
  }
}
