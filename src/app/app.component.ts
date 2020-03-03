import { Component } from '@angular/core';
import { ConfigService } from './app.service'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  constructor(private configService: ConfigService){}
  title = 'try-angular-flask';
  info = ""
  ngOnInit()
  {
    console.log(this.configService.getBasicInfo().subscribe((res:any)=>{console.log(res)}))
  }
}
