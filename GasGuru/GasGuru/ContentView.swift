//
//  ContentView.swift
//  GasGuru
//
//  Created by Rio Shintani on 6/1/24.
//

import SwiftUI
import AVFoundation

struct ContentView: View {
    let buttonText1 : String = "hello world"
    let buttonText2 : String = "welcome to Swift!"
    
    @State private var poop = [String]()
    
    var body: some View {
        NavigationStack(path: $poop) {
            /*
             VStack {
             MyButton(text: buttonText1, bezel: 10)
             MyButton(text: buttonText2, bezel: 10)
             }
             }
             }*/
            
            /*struct MyButton : View {
             var text : String
             var bezel : CGFloat
             
             var body: some View {
             Button{
             let utterance = AVSpeechUtterance(string: text)
             utterance.voice = AVSpeechSynthesisVoice(language: "en-gb")
             let synthesizer = AVSpeechSynthesizer()
             synthesizer.speak(utterance)
             
             }label: {
             Text(text)
             .fontWeight(.bold)
             .font(.system(.title, design: .rounded))
             .font(.title)
             
             }
             .padding()
             .foregroundColor(.yellow)
             .background(Color.red)
             .cornerRadius(bezel)
             }
             }*/
            
            
            ZStack {
                Color(.sRGB, red: 0.06275, green: 0.42353, blue: 0.23529)
                    .ignoresSafeArea()
                VStack(alignment: .leading, spacing: 20.0) {
                    Image("loading")
                        .resizable()
                        .aspectRatio(contentMode: .fill)
                        .cornerRadius(15)
                }.frame(maxWidth: .infinity, maxHeight: .infinity)
                
                
            }
            .onTapGesture {
                poop.append("Fart")
            }
            .navigationDestination(for: String.self) { str in
                ZStack {
                    Color(.sRGB, red: 0.06275, green: 0.42353, blue: 0.23529)
                        .ignoresSafeArea()
                    VStack(alignment: .leading, spacing: 20.0) {
                        Text("Sort: Cheap to Expensive")
                        Text("9.0 minutes away, 8.9 miles away, $1.36, '30375 SE High Point Way Issaquah, Washington")
                        Text("7.0 minutes away, 5.3 miles away, $3.14, '1479 NW Sammamish Rd Issaquah, Washington")
                        Text("5.0 minutes away, 1.6 miles away, $4.83, '157 NE Gilman Blvd, Issaquah, WA 98027")
                        Text("4.0 minutes away, 1.4 miles away, $9.00, '24 NW Holly St Issaquah, Washingtondiesel*365")
                        Text("")
                        Text("")
                        Text("Sort: Closest to Farthest")
                        Text("4.0 minutes away, 1.4 miles away, $9.00, '24 NW Holly St Issaquah, Washingtondiesel*365")
                        Text("5.0 minutes away, 1.6 miles away, $4.83, '157 NE Gilman Blvd, Issaquah, WA 98027")
                        Text("7.0 minutes away, 5.3 miles away, $3.14, '1479 NW Sammamish Rd Issaquah, Washington")
                        Text("9.0 minutes away, 8.9 miles away, $1.36, '30375 SE High Point Way Issaquah, Washington")
                        Text("")
                        Text("")
                        


                        
                        
                    }
                    
                }
                

            }
        }
        
    }
}
