import 'NavBar.dart';
import 'package:flutter/material.dart';

void main() {
  runApp(MaterialApp(
      home: Homepage(),
    theme: ThemeData(
      canvasColor: Color.fromRGBO(118, 176, 195, 100),
    )
  ));
}

// -------------------------------------------------------------------------- //
class Homepage extends StatefulWidget {
  @override
  _HomepageState createState() => _HomepageState();
}

class _HomepageState extends State<Homepage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: HomeForeground(
        expandedHeight: 153.0,
        appBarChild: Text('home Background'),
        appBarBackgroundColor:Color.fromRGBO(118, 176, 195, 100),
        fillChild: Text('drop-down, square buttons'),
        // fillColor:  Color.fromRGBO(240, 241, 226, 100),
        fillColor:  Color(0xfff9fbe7),
      ),
      bottomNavigationBar: NavBar(),
    );
  }
}
// -------------------------------------------------------------------------- //

// class Home extends StatelessWidget {
//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       body: HomeForeground(
//         expandedHeight: 153.0,
//         appBarChild: Text('home Background'),
//         appBarBackgroundColor:Color.fromRGBO(118, 176, 195, 100),
//         fillChild: Text('drop-down, square buttons'),
//         // fillColor:  Color.fromRGBO(240, 241, 226, 100),
//         fillColor:  Color(0xfff9fbe7),
//       ),
//       bottomNavigationBar: NavBar(),
//     );
//   }
// }

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
          backgroundColor:appBarBackgroundColor,
          expandedHeight: expandedHeight,
          floating: false,
          pinned: false,
          // title: appBarChild,
            flexibleSpace: FlexibleSpaceBar(
                background:HomeBackground(title: 'Home' , height:130.0)
            )
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
                // child: fillChild,
                  child: GridView.count(
                    crossAxisCount: 2,
                    children: List.generate(10, (index) {
                      return Center(
                        child: Text(
                          'Item $index',
                          style: Theme.of(context).textTheme.headline5,
                        ),
                      );
                    }),
                  )
              ),
            ),
          ),
        ),
      ],
    );
  }
}

class HomeBackground extends StatelessWidget {
  final title;
  final height;

  HomeBackground({this.title, this.height});

  @override
  Widget build(BuildContext context) {
    return Container(
      width: MediaQuery.of(context).size.width,
      height: height,
      color: Color.fromRGBO(94, 163, 184, 100),
      child: Stack(
        children: [
          Positioned(
            top: -47,
            left: -41,
            child: Square(
              color:  Color.fromRGBO(22, 111, 123, 100),
              size: 142.0,
              borderRadius: 31.0,
            ),
          ),
          Positioned(
            top: -37,
            left: 58,
            child: Square(
              color: Color.fromRGBO(169, 229, 238, 30),
              size: 93.0,
              borderRadius: 18.0,
            ),
          ),
          Positioned(
            top: 102,
            left : 30,
            child: FlatButton(
              onPressed: () {},
              child: Text(title,
                style: TextStyle(
                    fontSize: 20,
                    color: const Color(0xffe8e8e8),
                ),
              ),
            ),
          ),
          Positioned(
            top: 65,
            left: 260,
            child: Image(
              image: AssetImage('lib/images/pd_log_bg_small.png'),
              width: 100,
              height: 88,
            ),
          ),
        ],
      ),
    );
  }
}

class Square extends StatelessWidget {
  final color;
  final size;
  final borderRadius;

  Square({this.color, this.size, this.borderRadius});

  @override
  Widget build(BuildContext context) {
    return Container (
      width: size,
      height: size,
      decoration: BoxDecoration(
          color: color,
          borderRadius: BorderRadius.all(Radius.circular(borderRadius))
      ),
    );
  }
}