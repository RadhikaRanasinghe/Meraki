import 'package:detect_pd/views/widgets/results-background.dart';
import 'package:detect_pd/views/widgets/results-foreground.dart';
import 'package:flutter/material.dart';

class NegativeResultsPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      // building the negative result page body
      body: ResultsForeground(
          mainBackgroundColor: Colors.greenAccent,
          fillColor: Colors.cyan.shade800,
          resultImage: ResultBackground(
            resultBackgroundHeight: 460.0,
            resultBackgroundImage: 'assets/positiveBackground.png',
          ),
          //ResultBackground
          expandedHeight: 300.0,
          result: 'Parkinson\'s Disease \n Not Detected'), //ResultsForeground
    ); //Scaffold
  }
}
