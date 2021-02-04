import 'package:flutter/material.dart';

void main() => runApp(PositiveBackground());

class PositiveBackground extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Welcome to Flutter',
      home: Container(
        decoration: BoxDecoration(
            image: DecorationImage(
                image: AssetImage("images/NegativeBackground2.png"),
                fit: BoxFit.cover)),
        child: Scaffold(
          backgroundColor: Colors.transparent,
          // appBar: AppBar(
          //   elevation: 0,
          //   backgroundColor: Colors.transparent,
          //   title: Text('My App'),
          //   centerTitle: true,
          //   leading: IconButton(
          //       icon: Icon(
          //         Icons.list,
          //         color: Colors.white,
          //       ),
          //       onPressed: () {}),
          // ),
        ),
      ),
    );
  }
}




