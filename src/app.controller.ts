import {
  Controller,
  Post,
  UploadedFiles,
  UseInterceptors,
} from '@nestjs/common';
import { AppService } from './app.service';
import { FilesInterceptor } from '@nestjs/platform-express';
import { spawn } from 'child_process';

@Controller()
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Post()
  @UseInterceptors(FilesInterceptor('files'))
  async createOrto(@UploadedFiles() files): Promise<string> {
    console.log('files', files);
    const filePaths = files.map((file) => file.path);
    const process = spawn('python3', ['src/stitch.py', ...filePaths]);

    process.stdout.on('data', (data) => {
      console.log(`stdout: ${data}`);
    });

    process.stderr.on('data', (data) => {
      console.error(`stderr: ${data}`);
    });

    process.on('close', (code) => {
      console.log(`child process exited with code ${code}`);
    });

    return 'Ortophoplan';
  }
}
