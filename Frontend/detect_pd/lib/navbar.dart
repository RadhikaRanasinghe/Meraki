import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
          backgroundColor: Colors.teal,
          body: SafeArea(
            child: Container(
              decoration: BoxDecoration(
                borderRadius: BorderRadius.only(
                    topRight: Radius.circular(20.0),
                    topLeft: Radius.circular(20.0)),
                color: Colors.white,
              ),
              height: 60.0,
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: const <Widget>[
                  Icon(
                    Icons.help_outline,
                    color: Colors.black,
                    size: 34.0,
                  ),
                  Icon(
                    Icons.home_outlined,
                    color: Colors.black,
                    size: 34.0,
                  ),
                  Icon(
                    Icons.settings_outlined,
                    color: Colors.black,
                    size: 34.0,
                  ),
                ],
              ),
            ),
          )),
    );
  }
}
