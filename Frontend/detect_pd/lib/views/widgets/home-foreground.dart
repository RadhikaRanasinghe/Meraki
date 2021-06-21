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
    return Scaffold(
      backgroundColor: Colors.black,
      body: CustomScrollView(
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
              color: Colors.transparent,
              child: Container(
                color: Colors.transparent,
                child: Container(
                  width: MediaQuery.of(context).size.width,
                  height: MediaQuery.of(context).size.height,
                  decoration: fillColor,
                  child: Center(
                    child: fillChild,
                  ),
                ),
              ),
            ),
          ),
        ],
      ),
    );


    //   CustomScrollView(
    //   slivers: <Widget>[
    //     SliverAppBar(
    //       backgroundColor: appBarBackgroundColor,
    //       expandedHeight: expandedHeight,
    //       floating: false,
    //       pinned: false,
    //       flexibleSpace: FlexibleSpaceBar(
    //         background: appBarChild,
    //       ),
    //     ),
    //     SliverFillRemaining(
    //       child: Container(
    //         width: MediaQuery.of(context).size.width,
    //         height: MediaQuery.of(context).size.height,
    //         color: Colors.transparent,
    //         child: Container(
    //           color: Color.fromRGBO(94, 163, 184, 100),
    //           child: Container(
    //             width: MediaQuery.of(context).size.width,
    //             height: MediaQuery.of(context).size.height,
    //             decoration: fillColor,
    //             child: Center(
    //               child: fillChild,
    //             ),
    //           ),
    //         ),
    //       ),
    //     ),
    //   ],
    // );
  }
}
