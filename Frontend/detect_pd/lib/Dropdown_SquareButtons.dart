import 'package:flutter/material.dart';

import 'HomeButtons.dart';

void main(){
  runApp(AllButtons());
}

class AllButtons extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.grey,
      ),
      home: Scaffold(
        body: Column(
          children: [
            Padding(
              padding: const EdgeInsets.only(top: 48.0, left: 40.0, right: 32.0),
              child: CustomDropdown(text: "START TEST",),
            ),
            Padding(
                padding: const EdgeInsets.only(top: 100)
            ),
            Flexible(
              child: SquareButtons(
                link1: null,
                link2: null,
                link3: null,
                link4: null,
                padding: EdgeInsets.all(50.0),
                bodyMargin: EdgeInsets.all(0.0),
                buttonMargin: EdgeInsets.all(8.0),
                iconSize: 60.0,
                fontSize: 14.0,
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class CustomDropdown extends StatefulWidget {

  final String text;

  const CustomDropdown({Key key, @required this.text}) : super(key: key);

  @override
  _CustomDropdownState createState() => _CustomDropdownState();
}

class _CustomDropdownState extends State<CustomDropdown> {
  GlobalKey actionKey;
  double height, width, xPosition, yPosition;
  bool isDropdownOpened = false;
  OverlayEntry floatingDropdown;

  @override
  void initState() {
    actionKey = LabeledGlobalKey(widget.text);
    super.initState();
  }

  void findDropdownData() {
    RenderBox renderBox = actionKey.currentContext.findRenderObject();
    height = renderBox.size.height;
    width = renderBox.size.width;
    Offset offset = renderBox.localToGlobal(Offset.zero);
    xPosition = offset.dx;
    yPosition = offset.dy;
  }

  OverlayEntry _createFloatingDropdown() {
    return OverlayEntry(builder: (context) {
      return Positioned(
        left: xPosition,
        width: width,
        top: yPosition + height + 10,
        height: 4 * height + 40,
        child: Dropdown(
          itemHeight: height -14,
        ),
      );
    });
  }

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      key: actionKey,
      onTap: (){
        setState(() {
          if (isDropdownOpened) {
            floatingDropdown.remove();
          }else{
            findDropdownData();
            floatingDropdown = _createFloatingDropdown();
            Overlay.of(context).insert(floatingDropdown);
          }

          isDropdownOpened = !isDropdownOpened;
        });
      },
      child: Container(
        decoration: BoxDecoration(
          borderRadius: BorderRadius.circular(100),
          color: Colors.grey,
        ),
        padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 25),
        child: Row(
          children: [
            Padding(
              padding: EdgeInsets.only(left: 30.0),
            ),
            Icon(Icons.search_sharp, color: Colors.black,),
            Padding(
              padding: EdgeInsets.only(right: 30.0),
            ),
            Text(
              widget.text,
              style: TextStyle(color: Colors.white, fontSize: 22, fontWeight: FontWeight.w600),
            ),
            Spacer(),
            Icon(Icons.arrow_drop_down, color: Colors.white,)
          ],
        ),
      ),
    );
  }
}

class Dropdown extends StatelessWidget {

  final double itemHeight;

  const Dropdown({Key key, this.itemHeight}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        SizedBox(height: 5,),
        Material(
          elevation: 20,
          shape: ArrowShape(),
          child: Container(
            height: 2*itemHeight,
            decoration: BoxDecoration(
              borderRadius: BorderRadius.circular(8.0),
              color: Colors.transparent
            ),
            child: Column(
              children: [
                UploadPhoto(width: 250.0,
                    height: 50.12,
                    bodyMargin: const EdgeInsets.only(left:30.0, top:0.0,right:30.0,bottom:10.0),
                    padding: EdgeInsets.all(5.0),
                    elevation: 6.0,
                    link: null  // TODO: implement UploadPhoto function
                ),
                TakePhoto(width: 250.0,
                    height: 50.12,
                    bodyMargin: const EdgeInsets.only(top: 10.0),
                    padding: EdgeInsets.all(5.0),
                    elevation: 6.0,
                    link: null  // TODO: implement TakePhoto function
                ),
              ],
            ),
          ),
        )
      ],
    );
  }
}

class ArrowShape extends ShapeBorder {
  @override
  EdgeInsetsGeometry get dimensions => throw UnimplementedError();

  @override
  Path getInnerPath(Rect rect, {TextDirection textDirection}) {
    throw UnimplementedError();
  }

  @override
  Path getOuterPath(Rect rect, {TextDirection textDirection}) {
    return getClip(rect.size/1600);
  }

  @override
  void paint(Canvas canvas, Rect rect, {TextDirection textDirection}) {
  }

  @override
  ShapeBorder scale(double t) {
    throw UnimplementedError();
  }
}

Path getClip(Size size) {
  Path path = Path();

  path.moveTo(0, size.height);
  path.lineTo(size.width / 2, 0);
  path.lineTo(size.width, size.height);

  return path;
}


