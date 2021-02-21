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
      height: 80.0,
      decoration: BoxDecoration(
        borderRadius: BorderRadius.only(
            topRight: Radius.circular(40.0),
            topLeft: Radius.circular(40.0)),
        color: Colors.white,
        boxShadow: [
          BoxShadow(
            color: Colors.black.withOpacity(0.3),
            spreadRadius: 1,
            blurRadius: 1,
            offset: Offset(0, -3),
          ),
        ],
      ),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
        children: [
          FlatButton(
            onPressed: link1 ,
            child: Icon(
              Icons.help_outline,
              color: Colors.black,
              size: 40.0,
            ),
          ),
          FlatButton(
            onPressed: link2,
            child: Icon(
              Icons.home_outlined,
              color: Colors.black,
              size: 40.0,
            ),
          ),
          FlatButton(
            onPressed: link3,
            child: Icon(
              Icons.settings_outlined,
              color: Colors.black,
              size: 40.0,
            ),
          ),
        ],
      ),
    );
  }
}

