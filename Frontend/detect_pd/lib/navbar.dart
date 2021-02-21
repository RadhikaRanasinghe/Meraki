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
          body: Stack(
            children: [
              Positioned(
                bottom: 0,
                left: 0,
                child: NavBar(
                  link1: null,
                  link2: null,
                  link3: null,
                )
              ),
            ],
          ),
        ),
      );
  }
}

class NavBar extends StatelessWidget {
  final link1;
  final link2;
  final link3;

  NavBar({this.link1, this.link2, this.link3});

  @override
  Widget build(BuildContext context) {
    return Container(
      width: MediaQuery.of(context).size.width,
      height: 60.0,
      decoration: BoxDecoration(
        borderRadius: BorderRadius.only(
            topRight: Radius.circular(20.0),
            topLeft: Radius.circular(20.0)),
        color: Colors.white,
      ),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
        children: [
          FlatButton(
            onPressed: link1 ,
            child: Icon(
              Icons.help_outline,
              color: Colors.black,
              size: 34.0,
            ),
          ),
          FlatButton(
            onPressed: link2,
            child: Icon(
              Icons.home_outlined,
              color: Colors.black,
              size: 34.0,
            ),
          ),
          FlatButton(
            onPressed: link3,
            child: Icon(
              Icons.settings_outlined,
              color: Colors.black,
              size: 34.0,
            ),
          ),
        ],
      ),
    );
  }
}
