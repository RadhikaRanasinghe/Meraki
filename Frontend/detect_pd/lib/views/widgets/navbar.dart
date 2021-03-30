import 'package:flutter/material.dart';

class NavBar extends StatelessWidget {
  final backgroundColor;
  final link1;
  final link2;
  final link3;
  final iconSize = 40.0;
  final height = 80.0;
  final borderRadius = 40.0;

  NavBar({this.link1, this.link2, this.link3, this.backgroundColor});

  @override
  Widget build(BuildContext context) {
    return Container(
      color: backgroundColor,
      child: Container(
        width: MediaQuery.of(context).size.width,
        height: height,
        decoration: BoxDecoration(
          // borderRadius: BorderRadius.only(
          //     topRight: Radius.circular(borderRadius),
          //     topLeft: Radius.circular(borderRadius)),
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
              onPressed: link1,
              child: Icon(
                Icons.help_outline,
                color: Colors.black,
                size: iconSize,
              ),
            ),
            FlatButton(
              onPressed: link2,
              child: Icon(
                Icons.home_outlined,
                color: Colors.black,
                size: iconSize,
              ),
            ),
            FlatButton(
              onPressed: link3,
              child: Icon(
                Icons.settings_outlined,
                color: Colors.black,
                size: iconSize,
              ),
            ),
          ],
        ),
      ),
    );
  }
}
