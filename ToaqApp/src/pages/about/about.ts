import { Component ,ViewChild, ElementRef} from '@angular/core';
import { HttpClient, HttpEvent, HttpHandler, HttpInterceptor, HttpRequest } from '@angular/common/http';
import { NavController } from 'ionic-angular';
import { ColorService } from '../../providers/color-service';
import { LoadingController } from 'ionic-angular';
import { Observable } from 'rxjs/Rx';

declare var google; 

@Component({
  selector: 'page-about',
  templateUrl: 'about.html'
})
export class AboutPage {
  colors : any ; 
  @ViewChild('map') mapElement: ElementRef;
  map: any;
  locations : any ; 
  trafficlightGreen = 'assets/imgs/greenLights.png' ; 
  trafficlightYellow = 'assets/imgs/redLights.png' ; 
  trafficlightRed = 'assets/imgs/yellowLights.png' ; 

  counters = [] ; 
  counter0 = Math.floor(Math.random() * 4) ; 
  counter1 = Math.floor(Math.random() * 4) ; 
  counter2 = Math.floor(Math.random() * 4) ; 
  counter3 = Math.floor(Math.random() * 4) ; 
  first = 0 ; 

  subscription ; 
  constructor(public navCtrl: NavController , private http: HttpClient, public colorService: ColorService, public loadingCtrl: LoadingController) {
    this.colors = this.colorService.getColors() ; 

  }


  ionViewDidLoad(){
    this.loadMap();
  }
 
  loadMap(){
 
    let latLng = new google.maps.LatLng(21.418301, 39.877699);
 
    let mapOptions = {
      center: latLng,
      zoom: 15,
      mapTypeId: google.maps.MapTypeId.ROADMAP
    }
 
    this.map = new google.maps.Map(this.mapElement.nativeElement, mapOptions);
    // need to be collect from server :) ; 
    this.locations = this.getData() ; 
    
    

    let i = 0 ; 
    while ( i < this.locations.length ){
      var myLatlng = new google.maps.LatLng(this.locations[i].lat,this.locations[i].lng);
      var marker = new google.maps.Marker({
        position: myLatlng   , 
        map: this.map , 
        icon : 'assets/imgs/'+this.locations[i].status+'.gif'  
      })  ;

      i++; 
    }
    

  }
  
  counterChange() {

    
    Observable.interval(30000).subscribe(() =>{
      if ( this.counter0 == 3) 
    this.counter0 = 0 ; 
  else 
    this.counter0 = this.counter0++; 
  });
    
//

    Observable.interval(50000).subscribe(() =>{
      if ( this.counter1 == 3) 
    this.counter1 = 0 ; 
    else 
    this.counter1 = this.counter1++; 
});
//
    Observable.interval(90000).subscribe(() =>{
      if ( this.counter2 == 3) 
    this.counter2 = 0 ; 
    else 
    this.counter2 = this.counter2++; 
    });
//
    Observable.interval(80000).subscribe(() =>{
    if ( this.counter3 == 3) 
    this.counter3 = 0 ; 
    else 
    this.counter3 = this.counter3++; 
    });
    
    this.navCtrl.setRoot(this.navCtrl.getActive().component);
  }
  
  getData() {
    const endpoint = 'http://139.162.42.13:8080/get_statuses/';
    return this.http
        .get(endpoint)
        .map(res => res.json().main)
        .subscribe(res => {
          this.locations = res;
         });
  }

  
}
