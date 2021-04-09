import 'dart:async';
import 'package:detect_pd/views/ui/main.dart';
import 'package:flutter/material.dart';

class SplashScreen extends StatefulWidget {
  @override
  _SplashScreenState createState() => _SplashScreenState();
}

class _SplashScreenState extends State<SplashScreen> {
  @override
  void initState() {
    super.initState();
    // Setting the time duration for the splash screen
    Timer(
        Duration(seconds: 4),
        () => Navigator.pushReplacement(
            context, MaterialPageRoute(builder: (context) => HomePage()))); // Timer
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      // allowing widget to overflow to another widget
      body: Stack(
        fit: StackFit.expand,
        children: [
          Container(
            decoration: BoxDecoration(color: Color(0xFF0B9FB3)),
          ),  // Container
          Column(
            mainAxisAlignment: MainAxisAlignment.start,
            children: [
              Expanded(
                flex: 2,
                child: Container(
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Image.asset(
                        // assigning the image logo
                        'assets/pd_log_bg_small.png',
                        height: 150.0,
                        width: 150.0,
                      ) // Image.asset
                    ],
                  ),  // Column
                ),  // Container
              ),  // Expanded
              Expanded(
                flex: 1,
                child: Column(
                  // makes widget into the center of the body
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                      // CircularProgressIndicator() // CircularProgressIndicator(),
                    Padding(
                      padding: EdgeInsets.only(top: 20.0),
                    ),  // Padding
                    Text(
                      "from",
                      style: TextStyle(
                          color: Colors.white,
                          fontSize: 18.0,
                          fontWeight: FontWeight.bold), // TextStyle
                    ),  // Text
                    Text(
                      "Meraki",
                      style: TextStyle(
                          color: Colors.white,
                          fontSize: 18.0,
                          fontWeight: FontWeight.bold), // TextStyle
                    ) // Text
                  ],
                ),  // Column
              ) // Expanded
            ],
          ) // Column
        ],
      ),  // Stack
    );  // Scaffold
  }
}
