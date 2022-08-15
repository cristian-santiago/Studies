class Sensor

    def self.install
        puts "Installing sensor."
        Sensor.new
    end

    def self.initiate
        puts "Initiating sensor."
        Sensor.new
    end
    
    def self.collect_metrics
        puts "Collecting metrics."
        puts "Analysing metrics."
        Sensor.new
    end
end

class TemperatureSensor < Sensor
    def self.collect_metrics
        puts "Collecting temperature metrics."
        Sensor.new
        super
    end
end


sens = Sensor.install
sens = Sensor.initiate
sens = Sensor.collect_metrics

p sens