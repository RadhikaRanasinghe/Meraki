import 'package:flutter/material.dart';
import 'package:showcaseview/showcase_widget.dart';
import 'package:showcaseview/showcaseview.dart';

class Detail extends StatefulWidget {
  @override
  _DetailState createState() => _DetailState();
}

class _DetailState extends State<Detail> {
  final GlobalKey _one = GlobalKey();
  BuildContext myContext;

  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addPostFrameCallback((_) {
      Future.delayed(Duration(milliseconds: 200),
              () => ShowCaseWidget.of(myContext).startShowCase([_one]));
    });
  }

  @override
  Widget build(BuildContext context) {
    return ShowCaseWidget(
      builder: Builder(
        builder: (context) {
          myContext = context;
          return Scaffold(
            appBar: AppBar(
              backgroundColor: Colors.transparent,
              elevation: 0,
              leading: IconButton(
                icon: Icon(
                  Icons.arrow_back,
                  color: Colors.black,
                ),
                onPressed: () {
                  Navigator.pop(context);
                },
              ),
            ),
            body: Padding(
              padding: const EdgeInsets.all(16.0),
              child: ListView(
                children: <Widget>[
                  Showcase(
                    key: _one,
                    title: 'Title',
                    description: 'Desc',
                    child: InkWell(
                      onTap: () {},
                      child: Text(
                        '',
                        style: TextStyle(
                            fontSize: 25, fontWeight: FontWeight.w600),
                      ),
                    ),
                  ),
                  SizedBox(
                    height: 16,
                  ),
                  Text(
                    '',
                    style: TextStyle(fontSize: 18, fontWeight: FontWeight.w500),
                  ),
                  SizedBox(
                    height: 16,
                  ),
                  RichText(
                    text: TextSpan(
                      style: TextStyle(
                          fontWeight: FontWeight.w400, color: Colors.black),
                      children: [
                        TextSpan(text: ''),
                        TextSpan(
                            text:
                            ''),
                        TextSpan(
                            text: '',
                            style: TextStyle(
                                fontWeight: FontWeight.w600,
                                color: Colors.black)),
                        TextSpan(
                            text:
                            ''),
                      ],
                    ),
                  ),
                ],
              ),
            ),
          );
        },
      ),
    );
  }
}
