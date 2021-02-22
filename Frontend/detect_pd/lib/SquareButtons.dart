import 'package:flutter/material.dart';

void main(List<String> args) {
  runApp(new MaterialApp(
    home: MyApp(),
  ));
}

class MyApp extends StatefulWidget {
  @override
  _MyAppState createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: new AppBar(
        title: Text("SQUARE BUTTONS"),
        backgroundColor: Colors.green[700],
      ),
      backgroundColor: Colors.yellow[100],
      body: Container(
        padding: EdgeInsets.all(30.0),
        margin: EdgeInsets.only(top:180),
        child: GridView.count(
            crossAxisCount: 2,
            children: <Widget>[
              Card(
                margin: EdgeInsets.all(8.0),
                child: InkWell(
                  onTap: (){
                    print("Download Template");
                  },
                  splashColor: Colors.green,
                  child: Center(
                    child: Column(
                      mainAxisSize: MainAxisSize.min,
                      children: <Widget>[
                        Icon(Icons.file_download, size: 70.0,),
                        Text("Downlod Template", style: new TextStyle(fontSize: 17.0),)
                      ],
                    ),
                  ),
                ),
              ),
              Card(
                margin: EdgeInsets.all(8.0),
                child: InkWell(
                  onTap: (){
                    print("About PD");
                  },
                  splashColor: Colors.green,
                  child: Center(
                    child: Column(
                      mainAxisSize: MainAxisSize.min,
                      children: <Widget>[
                        Icon(Icons.menu_book_sharp, size: 70.0,),
                        Text("About PD", style: new TextStyle(fontSize: 17.0),)
                      ],
                    ),
                  ),
                ),
              ),
              Card(
                margin: EdgeInsets.all(8.0),
                child: InkWell(
                  onTap: (){
                    print("User Guide");
                  },
                  splashColor: Colors.green,
                  child: Center(
                    child: Column(
                      mainAxisSize: MainAxisSize.min,
                      children: <Widget>[
                        Icon(Icons.find_in_page_rounded, size: 70.0,),
                        Text("User Guide", style: new TextStyle(fontSize: 17.0),)
                      ],
                    ),
                  ),
                ),
              ),
              Card(
                margin: EdgeInsets.all(8.0),
                child: InkWell(
                  onTap: (){
                    print("FAQ");
                  },
                  splashColor: Colors.green,
                  child: Center(
                    child: Column(
                      mainAxisSize: MainAxisSize.min,
                      children: <Widget>[
                        Icon(Icons.headset_mic_rounded, size: 70.0,),
                        Text("FAQ", style: new TextStyle(fontSize: 17.0),)
                      ],
                    ),
                  ),
                ),
              ),
            ],
        ),
      ),
    );
  }
}
