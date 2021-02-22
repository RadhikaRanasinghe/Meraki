import 'dart:developer';
import 'detailScreen.dart';
import 'package:flutter/material.dart';
import 'package:showcaseview/showcaseview.dart';

void main() => runApp(MyApp());

//Todo : Make the guide run only once at the start of the app -
// Todo : Hint :- SharedPreferences

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter ShowCase',
      home: Scaffold(
        body: ShowCaseWidget(
          onStart: (index, key) {
            log('onStart: $index, $key');
          },
          onComplete: (index, key) {
            log('onComplete: $index, $key');
          },
          builder: Builder(builder: (context) => HomePage()),
          autoPlay: false,
          autoPlayDelay: Duration(seconds: 3),
          autoPlayLockEnable: false,
        ),
      ),
    );
  }
}

class HomePage extends StatefulWidget {
  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  GlobalKey _one = GlobalKey();
  GlobalKey _two = GlobalKey();
  GlobalKey _three = GlobalKey();
  // GlobalKey _four = GlobalKey();
  // GlobalKey _five = GlobalKey();

  @override
  void initState() {
    super.initState();
    //Start showcase view after current widget frames are drawn.
    WidgetsBinding.instance.addPostFrameCallback((_) =>
        ShowCaseWidget.of(context)
            .startShowCase([_one, _two, _three]));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: ListView(
          children: <Widget>[
            Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: <Widget>[
                Container(
                  padding: const EdgeInsets.only(top: 8, left: 8, right: 8),
                  child: Card(
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(10),
                    ),
                    elevation: 3,
                    child: Container(
                      padding: const EdgeInsets.all(8),
                      child: Row(
                        children: <Widget>[
                          Expanded(
                            child: Row(
                              children: <Widget>[
                                CustomShowcaseWidget(
                                    globalKey: _one,
                                    description: 'Print the template and trace on it to take test',
                                    child: Container(
                                      width: 30,
                                      height: 30,
                                      decoration: BoxDecoration(
                                        shape: BoxShape.circle,
                                      ),
                                    ),
                                ),
                                SizedBox(
                                  width: 10,
                                ),
                              ],
                            ),
                          ),
                          CustomShowcaseWidget(
                            globalKey: _two,
                            description:
                            'Take test after drawing hand trace',
                            child: Container(
                              width: 30,
                              height: 30,
                              decoration: BoxDecoration(
                                shape: BoxShape.circle,
                              ),
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                ),
                SizedBox(
                  height: 7,
                ),
                Container(
                  padding: const EdgeInsets.only(left: 16, top: 4),
                  child: Text(
                    'Guided approach demo',
                    style: TextStyle(
                      color: Colors.black54,
                      fontSize: 15,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                ),
              ],
            ),
            Padding(padding: EdgeInsets.only(top: 8)),
            GestureDetector(
                onTap: () {
                  Navigator.push(
                    context,
                    MaterialPageRoute(
                      builder: (_) => Detail(),
                    ),
                  );
                },
                child: Container(
                  padding: const EdgeInsets.symmetric(vertical: 8),
                  child: CustomShowcaseWidget(
                    globalKey: _three,
                    description:
                    'This is the user guide for DetectPD.',
                    child: Container(
                      width: 30,
                      height: 30,
                      decoration: BoxDecoration(
                        shape: BoxShape.circle,
                      ),
                    ),
                  ),
                )),
          ],
        ),
      ),
    );
  }
}

class CustomShowcaseWidget extends StatelessWidget {
  final GlobalKey globalKey;
  final String description;
  final Widget child;

  const CustomShowcaseWidget({
    @required this.globalKey,
    @required this.description,
    @required this.child,
  });

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
    // overlayOpacity: 0.7,
    child: child,
  );
}