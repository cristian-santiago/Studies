class Sensor
    def install
        puts "Installing sensor."
    end

    def initiate
        puts "Initiating sensor."
    end
    
    def collect_metrics
        puts "Collecting metrics."
        puts "Analysing metrics."
    end
end

class TemperatureSensor < Sensor
    def collect_metrics
        puts "Collecting temperature metrics."
        super
    end
end

sens = TemperatureSensor.new
sens.install
sens.initiate
sens.collect_metrics