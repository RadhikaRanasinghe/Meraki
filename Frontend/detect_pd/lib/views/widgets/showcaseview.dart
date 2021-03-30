import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:showcaseview/showcase.dart';

class CustomShowcaseWidget extends StatelessWidget {
  final GlobalKey globalKey;
  final String description;
  final Widget child;

  const CustomShowcaseWidget(
      {@required this.globalKey,
        @required this.description,
        @required this.child});

  @override
  Widget build(BuildContext context) => Showcase(
    key: globalKey,

    showcaseBackgroundColor: Colors.teal[300],
    contentPadding: EdgeInsets.all(25),
    // showArrow: false,
    disableAnimation: false,
    // title: 'Hello',
    // titleTextStyle: TextStyle(color: Colors.white, fontSize: 32),
    description: description,
    descTextStyle: TextStyle(
      color: Colors.indigo[900],
      fontWeight: FontWeight.bold,
      fontSize: 16,
    ),
    // overlayColor: Colors.white,
    overlayOpacity: 0.0,
    child: child,
  );
}