import 'package:flutter/material.dart';

void main() {
  runApp(MaterialApp(
      home: Home()
  ));
}

class Home extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: HomeForeground(
        expandedHeight: 153.0,
        appBarChild: Text('home Background'),
        appBarBackgroundColor: Color.fromRGBO(94, 163, 184, 100),
        fillChild: Text('drop-down, square buttons'),
        fillColor:  Color.fromRGBO(240, 241, 226, 100),
      )
    );
  }
}

class HomeForeground extends StatelessWidget {
  final expandedHeight;
  final appBarChild;
  final appBarBackgroundColor;
  final fillChild;
  final fillColor;

  HomeForeground({this.expandedHeight, this.appBarBackgroundColor, this.appBarChild, this.fillChild, this.fillColor});

  @override
  Widget build(BuildContext context) {
    return CustomScrollView(
      slivers: <Widget>[
        SliverAppBar(
          backgroundColor: appBarBackgroundColor,
          expandedHeight: expandedHeight,
          floating: false,
          pinned: false,
          title: appBarChild,
        ),
        SliverFillRemaining(
          child: Container(
            width: MediaQuery.of(context).size.width,
            height: MediaQuery.of(context).size.height,
            color: appBarBackgroundColor,
            child: Container(
              width: MediaQuery.of(context).size.width,
              height: MediaQuery.of(context).size.height,
              decoration: BoxDecoration(
                  color: fillColor,
                  borderRadius: BorderRadius.only(
                      topLeft: Radius.circular(40),
                      topRight: Radius.circular(40)
                  ),
              ),
              child: Center(
                child: fillChild,
              ),
            ),
          ),
        ),
      ],
    );
  }
}
