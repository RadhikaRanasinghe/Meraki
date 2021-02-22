import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        canvasColor: Colors.transparent,
      ),
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  String _selectedItem = '';

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
          image: DecorationImage(
              image: AssetImage("lib/images/PositiveBackground2.png"),
              fit: BoxFit.cover)),
      child: Scaffold(
        backgroundColor: Colors.transparent,
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              RaisedButton(
                child: Text('Show'),
                onPressed: () => _onButtonPressed(),
              ),
              Text(
                _selectedItem,
                style: TextStyle(fontSize: 30),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Align _buildBottomNavigationMenu() {
    // return Column(
    //   mainAxisSize: MainAxisSize.min,
    //   children: <Widget>[
    return Align(alignment: Alignment.bottomCenter,
        child: Container(
          width: 400.0,
          // height: 447.0,
          child: Column(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children:<Widget>[
                SizedBox(
                  // width: 450.0,
                  // height: 45.0,
                  child: Text(
                    'Results',
                    style: TextStyle(
                      fontFamily: 'Montserrat',
                      fontSize: 31,
                      color: const Color(0xffe8e8e8),
                      fontWeight: FontWeight.w700,
                      height: 0.6967741443264869,
                    ),
                    textAlign: TextAlign.center,
                  ),
                ),
                SizedBox(
                  // width: 450.0,
                  // height: 131.0,
                  child: Text(
                    'Parkinson\'s Disease \nNot Detected!',
                    style: TextStyle(
                      fontFamily: 'Montserrat',
                      fontSize: 28,
                      color: const Color(0xffffffff),
                      fontWeight: FontWeight.w700,
                      height: 1.4285714285714286,
                    ),
                    textAlign: TextAlign.center,
                  ),
                ),
                SizedBox(
                  // width: 450.0,
                  child: Text(
                    'Disclaimer: Consult a medical professional for further clarification ',
                    style: TextStyle(
                      fontFamily: 'Montserrat',
                      fontSize: 10,
                      color: const Color(0xffffffff),
                      fontWeight: FontWeight.w700,
                      // height: 2.1599998474121094,
                    ),
                    textAlign: TextAlign.center,
                  ),
                )
              ]
          ),
          decoration: BoxDecoration(
            borderRadius: BorderRadius.only(
              topLeft: const Radius.circular(50),
              topRight: const Radius.circular(50),
              // topLeft: Radius.circular(40.0),
              // topRight: Radius.circular(40.0),
            ),
            color: const Color(0xFF006064),
          ),
        )
    );
  }

  void _onButtonPressed() {
    showModalBottomSheet(
        context: context,
        builder: (context) {
          return Container(
              color: Colors.transparent,
              child: Container(
                child: _buildBottomNavigationMenu(),
                // color: Colors.transparent,
                height: 360,
                decoration: BoxDecoration(
                  color: Theme.of(context).canvasColor,
                  borderRadius: BorderRadius.only(
                    topLeft: const Radius.circular(50),
                    topRight: const Radius.circular(50),
                  ),
                ),
              )
          );
        });
  }

  void _selectItem(String name) {
    Navigator.pop(context);
    setState(() {
      _selectedItem = name;
    });
  }
}
