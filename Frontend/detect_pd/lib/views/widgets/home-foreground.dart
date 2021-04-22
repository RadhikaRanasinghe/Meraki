import 'package:flutter/material.dart';

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
          flexibleSpace: FlexibleSpaceBar(
            background: appBarChild,
          ),
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
                  // borderRadius: BorderRadius.only(
                  //     topLeft: Radius.circular(40),
                  //     topRight: Radius.circular(40)
                  // ),
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
